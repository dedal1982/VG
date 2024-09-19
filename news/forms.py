from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django.utils.translation import gettext_lazy as _

from news.models import Article


class NewsForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditor5Widget(), label="Текст статьи", required=False
    )

    class Meta:
        model = Article
        fields = "__all__"
        exclude = [
            "is_published",
            "published_date",
            "updated_date",
            "views",
            "author",
            "slug",
        ]
        labels = {
            "title": _("Загаловок статьи"),
            "subcontent": _("Подзаголовок"),
            "content": _("Текст статьи"),
            "photo": _("Фото"),
            "category": _("Категории"),
        }
        error_messages = {
            "name": {
                "max_length": _("This writer's name is too long."),
            },
        }
        widgets = {
            "content": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="comment"
            ),
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "subcontent": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "photo": forms.FileInput(
                attrs={"class": "form-control-file", "required": True}
            ),
            "tags": forms.SelectMultiple(attrs={"class": "form-control"}),
        }


class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditor5Widget())

    class Meta:
        model = Article
        fields = "__all__"
