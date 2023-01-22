from django.db import models


class Post(models.Model):
    meta_title = models.CharField(max_length=100, blank=True)
    meta_description = models.CharField(max_length=200, blank=True)
    og_image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=127)
    slug = models.SlugField(max_length=127, unique=True)
    content = models.TextField()
