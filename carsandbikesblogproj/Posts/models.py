from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


# Create your models here.
class Post(models.Model):
    post_title= models.CharField(max_length=255)
    post_description = models.TextField()
    post_shortname = models.SlugField(max_length=255, unique=True)
    post_publish_datatime = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(upload_to='post/images/')
    category = models.ForeignKey(Category, default=1, related_name='post_category', on_delete=models.CASCADE)

    def __str__(self):
        return self.post_shortname

