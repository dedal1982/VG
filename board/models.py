from django.db import models
from django.urls import reverse

from users.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Listing(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активен'),
        ('sold', 'Продан'),
        ('archived', 'В архиве'),
    ]
    STATUS_CONDITIONS = {
        'new': 'Новый',
        'used': 'Б/У',
    }
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='listings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='listings', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    condition = models.CharField(max_length=20, choices=STATUS_CONDITIONS.items(), default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        
        return self.title
    
    def get_absolute_url(self):
        return reverse("listing_detail", args=[self.created_at.year, self.created_at.month, self.created_at.day, self.slug])

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"
        unique_together = (('user', 'slug'))
        ordering = ['-created_at']

class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='listing_images/%Y/%m/%d/%H')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ['order']
        unique_together = (('listing', 'order'),)
        

    def __str__(self):
        return f"Image {self.order} for {self.listing.title}"

class Application(models.Model):
    listing = models.ForeignKey(Listing, related_name='applications', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']

    def __str__(self):
        return f"Application from {self.user.username} for {self.listing.title}"
