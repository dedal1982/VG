from django import template

from news.models import Article

register = template.Library()


@register.inclusion_tag("news/last_news_rightbar.html")
def load_most_news():
    last_news = Article.objects.with_cats().order_by("-published_date")[:5]
    return {"last_news": last_news}
