from django import template
from django.db import models

from news.models import Category

register = template.Library()


@register.simple_tag()
def get_categories():
    return (
        Category.objects.values("name")
        .annotate(count=models.Count("articles__id"))
        .order_by("-count")
    )
