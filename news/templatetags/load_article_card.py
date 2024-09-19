from django import template

from news.models import Article

register = template.Library()


@register.inclusion_tag("news/article_card.html")
def load_article_card(article: Article):
    return {"article": article}
