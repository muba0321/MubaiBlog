from django.urls import path

from Blog_article.views.article import article_list, article_detail, article_create, article_update, article_delete
from Blog_article.views.comment import comment_list, comment_detail, comment_create, comment_update, comment_delete
from Blog_article.views.user import user_list, user_detail, user_create, user_update, user_delete

urlpatterns = [
    # 用户相关 URL
    path('users/', user_list, name='user_list'),
    path('users/<int:user_id>/', user_detail, name='user_detail'),
    path('users/create/', user_create, name='user_create'),
    path('users/<int:user_id>/update/', user_update, name='user_update'),
    path('users/<int:user_id>/delete/', user_delete, name='user_delete'),

    # 文章相关 URL
    path('articles/', article_list, name='article_list'),
    path('articles/<int:article_id>/', article_detail, name='article_detail'),
    path('articles/create/', article_create, name='article_create'),
    path('articles/<int:article_id>/update/', article_update, name='article_update'),
    path('articles/<int:article_id>/delete/', article_delete, name='article_delete'),

    # 评论相关 URL
    path('comments/', comment_list, name='comment_list'),
    path('comments/<int:comment_id>/', comment_detail, name='comment_detail'),
    path('comments/create/', comment_create, name='comment_create'),
    path('comments/<int:comment_id>/update/', comment_update, name='comment_update'),
    path('comments/<int:comment_id>/delete/', comment_delete, name='comment_delete'),
]
