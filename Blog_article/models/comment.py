from django.db import models
from .user import User
from .article import Article


class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    is_deleted = models.BooleanField(default=False, verbose_name='已删除')

    class Meta:
        db_table = 'blog_comment'

    def __str__(self):
        return self.content
