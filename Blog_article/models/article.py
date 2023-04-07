from django.db import models
from .user import User


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True, related_name='articles')
    is_deleted = models.BooleanField(default=False, verbose_name='已删除')

    class Meta:
        db_table = 'blog_article'

    def __str__(self):
        return self.title
