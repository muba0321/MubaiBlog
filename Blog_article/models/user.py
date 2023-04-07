from importlib.resources import _

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager, Permission, Group
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    is_deleted = models.BooleanField(default=False, verbose_name='已删除')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        db_table = 'blog_article_user'

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions '
                    'granted to each of their groups.'),
        related_name='blog_article_user_set',  # 添加 related_name 参数
        related_query_name='user',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='blog_article_user_set',  # 添加 related_name 参数
        related_query_name='user',
    )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'blog_article_user'

