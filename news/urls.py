from django.urls import path

from news import views


urlpatterns = [
    path("", views.get_home_page, name="news_home"),
    path("add-comment/", views.add_comment, name="add_comment"),
    path("create/", views.add_a_new_post, name="post_create"),
    path("search/", views.get_search_result, name="news_search"),
    path(
        "category/<slug:category_slug>/",
        views.get_category_page,
        name="category_detail",
    ),
    path("<slug:slug>/", views.get_single_post, name="article_detail"),
]
