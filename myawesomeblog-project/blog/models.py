from django.db import models


class Post(models.Model):
    post_headline = models.CharField(max_length=200)
    post_date = models.DateTimeField()
    post_text = models.TextField()
    post_image = models.ImageField(upload_to='./post_images/') #куда загружать изображения

    def get_summary(self):
        if len(self.post_text) > 60:
            return self.post_text[:60]+'...'
        else:
            return self.post_text

    #устанавливаю в админке записям отображение заголовков
    def __str__(self):
        return self.post_headline
# Create your models here.
