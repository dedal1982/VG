from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from users.models import User
from django.utils.text import slugify
from django.urls import reverse

#    from django.db.backends.mysql.indexes import FullTextIndex


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", args=[self.slug])


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("tag_detail", args=[self.slug])


class ArticleManager(models.Manager):
    def with_cats(self):
        return self.select_related("category")


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="articles")
    subcontent = models.CharField(max_length=200)
    content = CKEditor5Field(max_length=5000)
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category, related_name="articles", on_delete=models.SET_NULL, null=True
    )
    tags = models.ManyToManyField(Tag, related_name="articles")
    views = models.PositiveIntegerField(default=0)
    photo = models.ImageField(upload_to="news/", blank=True, null=True)
    objects = ArticleManager()

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["-published_date"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", args=[self.slug])


class Comment(models.Model):
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="replied_comments",
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_date"]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.article.title}"
