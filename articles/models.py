from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from tinymce.models import HTMLField

CustomUser = get_user_model()


class Article(models.Model):
    DRAFT = 'draft'
    PUBLISHED = 'published'

    CAT_ARTICLE = 'cat_article'
    CAT_RECIPE = 'cat_recipe'

    ARTICLE_STATUS_CHOICES = [
        (DRAFT, 'Draft'),
        (PUBLISHED, 'Published')
    ]

    ARTICLE_TYPE_CHOICES = [
        (CAT_ARTICLE, 'Article'),
        (CAT_RECIPE, 'Recipe'),
    ]

    title = models.CharField(max_length=200, unique=True)
    subtitle = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True)
    body = HTMLField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='article_posts')
    featured_image = models.ImageField(upload_to='images/', blank=True)
    featured_image_caption = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS_CHOICES, default=DRAFT)
    type = models.CharField(max_length=20, choices=ARTICLE_TYPE_CHOICES, default=CAT_ARTICLE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:article_detail', kwargs={'slug': self.slug})
