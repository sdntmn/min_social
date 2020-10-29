from django.db import models
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Дата публикации", auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", verbose_name="Автор")
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, related_name="posts", verbose_name="Группа", blank=True, null=True)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        # выводим текст поста
        return f'{self.text}'


#

 #   firstname = forms.CharField(label="Введите имя", initial='Text')
  #  lastname = forms.CharField(label="Введите фамилию", initial='Text')