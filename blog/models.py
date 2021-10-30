from django.db import models


class Post(models.Model):
    post_headline = models.CharField(max_length=200)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='./post_images/') #куда загружать изображения


# Create your models here.
