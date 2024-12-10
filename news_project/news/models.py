from django.db import models


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField('Название новости', max_length=100)
    description = models.TextField('Краткое описание', max_length=200)
    news_text = models.TextField('Текст новости')
    news_date=models.DateTimeField('Дата публикации')