from django.contrib import admin
from django.utils.text import slugify

from news.models import Article, Category, Comment, Tag
from .forms import NewsAdminForm


class ArticleAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = (
        "title",
        "author",
        "category",
        "published_date",
        "updated_date",
        "views",
    )
    list_filter = ("author", "category", "tags", "published_date")
    search_fields = ("title", "content", "author__username")
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Tag)
