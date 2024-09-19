from datetime import datetime, timedelta
import json
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404, redirect, render
from django.db import models
from django.db.models import Q
from django.views.decorators.http import require_POST

from news.forms import NewsForm
from news.models import Article, Category, Comment, Tag
from django.core.paginator import Paginator


def get_home_page(request: HttpRequest):
    now = datetime.now()
    last_7_days = now - timedelta(days=7)
    most_viewed_all_time = Article.objects.with_cats().order_by("-views")[:6]
    most_viewed_last_week = (
        Article.objects.with_cats()
        .filter(published_date__gte=last_7_days)
        .order_by("-views")[:6]
    )
    most_last_posts = Article.objects.with_cats().order_by("-published_date")[:5]
    banner_news = most_viewed_all_time[:2]
    popular_tags = (
        Tag.objects.values("name")
        .annotate(count=models.Count("articles__id"))
        .order_by("-count")
    )
    return render(
        request,
        "news/home.html",
        {
            "banner_news": banner_news,
            "most_viewed_all_time": most_viewed_all_time,
            "most_viewed_last_week": most_viewed_last_week,
            "most_last_posts": most_last_posts,
            "most_viewed_first": most_viewed_all_time[0],
            "most_viewed_first_2": most_viewed_all_time[1:3],
            "most_viewed_second": most_viewed_all_time[3],
            "most_viewed_second_2": most_viewed_all_time[4:6],
            "popular_tags": popular_tags[:10],
        },
    )


def get_single_post(request: HttpRequest, slug: str):
    post = get_object_or_404(Article, slug=slug)
    similar_posts = (
        Article.objects.prefetch_related("comments", "tags")
        .filter(tags__in=post.tags.values_list("id", flat=True))
        .exclude(id=post.id)
        .annotate(count=models.Count("tags"))
        .order_by("-count", "-published_date")
    )
    tags = Tag.objects.filter(articles__id=post.id)
    comments = Comment.objects.filter(article_id=post.id)
    return render(
        request,
        "news/single.html",
        {
            "post": post,
            "similar_posts": similar_posts,
            "tags": tags,
            "comments": comments,
        },
    )


@require_POST
def add_comment(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("login", permanent=True)
    comment_data = json.loads(request.body) | {"user": request.user}
    new_comment = Comment.objects.create(**comment_data)
    json_answer = serialize("json", [new_comment])
    answer = json.loads(json_answer)
    answer = answer[0]["fields"] | {"id": answer[0].get("pk")}
    return JsonResponse(answer, safe=False)


def add_a_new_post(request: HttpRequest):
    if not request.user.is_authenticated:
        return redirect("login", permanent=True)
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect("home")
        else:
            return render(request, "news/create_post.html", {"form": form})

    return render(request, "news/create_post.html", {"form": NewsForm})


def get_search_result(request: HttpRequest):
    search = request.GET.get("s")

    articles = Article.objects.with_cats()
    if search:
        articles = articles.filter(
            Q(title__contains=search)
            | Q(content__contains=search)
            | Q(subcontent__contains=search)
        ).order_by("-published_date")[:10]
    return render(
        request,
        "news/category_filter.html",
        {"articles": articles, "key": search, "filter_by": "search"},
    )


def get_category_page(request: HttpRequest, category_slug: str):
    category = get_object_or_404(Category, slug=category_slug)
    articles = category.articles.with_cats()
    paginator = Paginator(articles, 4)
    page_number = request.GET.get("page")
    page_articles = paginator.get_page(page_number)
    return render(
        request,
        "news/category_filter.html",
        {"key": category.name, "articles": page_articles, "filter_by": "category"},
    )
