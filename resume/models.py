from django.db import models

# Create your models here.
from django.db import models
from django_jalali.db import models as jmodels
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISH = "PB", "Publish"
        DELETE = "DL", "Delete"
    objects = jmodels.jManager()
    title = models.CharField(max_length=255, verbose_name='موضوع')
    description = models.TextField(verbose_name='توضیحات')
    writer = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="post_writer", null=True, verbose_name='نویسنده')
    category = models.CharField(max_length=255, verbose_name='دسته بندی')
    created = jmodels.jDateTimeField(auto_now_add=True)
    modified = jmodels.jDateTimeField(auto_now=True)
    publish = jmodels.jDateTimeField(
        default=timezone.now, verbose_name='زمان انتشار')
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name='وضعیت')

    class Meta:
        indexes = [models.Index(fields=['title'])]
        verbose_name = 'پست'
        verbose_name_plural = 'پست ها'

    def __str__(self) -> str:
        return self.title


class ImagePost(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="images", verbose_name='پست')
    title = models.CharField(max_length=255, verbose_name='موضوع')
    image = models.ImageField(upload_to='image/', verbose_name='مسیر')

    class Meta:
        indexes = [models.Index(fields=['title'])]
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصویر ها'

    def __str__(self) -> str:
        return self.post.title


class CommentPost(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    comment_text = models.TextField(verbose_name='متن')
    created = jmodels.jDateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد')
    modified = jmodels.jDateTimeField(
        auto_now=True, verbose_name='تاریخ اپدیت')

    comment_post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comment", verbose_name='پست')
    comment_status = models.BooleanField(default=False, verbose_name='انتشار')
    date_comment = jmodels.jDateTimeField(
        default=timezone.now, verbose_name='زمان ')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرها'

    def __str__(self) -> str:
        return f'{self.comment_post.title} : {self.comment_text}'
