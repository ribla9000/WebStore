import datetime
from django.db import models
from django.utils import timezone
from django.db import models
from tinymce.models import HTMLField


# class Film(models.Model):
#     title = models.CharField(max_length=200)
#     exerpt = models.TextField(max_length=200)
#     content = HTMLField()

# Create your models here.
class Article(models.Model):
	
	article_title = models.CharField('название статьи',max_length = 200)
	article_text = models.TextField('текст статьи')
	pub_date =  models.DateTimeField('дата публикации')




	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))


class Comment(models.Model):
	
	article = models.ForeignKey(Article, on_delete= models.CASCADE )
	author_name = models.CharField('Иия автора', max_length = 50)
	comment_text = models.CharField('Текст комментария', max_length = 200)

	def __str__(self):
		return self.author_name