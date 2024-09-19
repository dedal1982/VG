from django.contrib import admin

from board.models import Listing, ListingImage, Category, Application
from django.utils.text import slugify


class ListingAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "user",
        "status",
        "condition",
        "created_at",
        "updated_at",
    )
    list_filter = ("user", "category", "status", "condition")
    search_fields = ("title", "description", "user__username")
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.title)
        super().save_model(request, obj, form, change)

admin.site.register(Listing, ListingAdmin)
admin.site.register(ListingImage)
admin.site.register(Category)
admin.site.register(Application)