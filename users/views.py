from django.shortcuts import render

#  импортируем CreateView, чтобы создать ему наследника
from django.views.generic import CreateView

#  функция reverse_lazy позволяет получить URL по параметру "name" функции path()
#  берём, тоже пригодится
from django.urls import reverse_lazy

#  импортируем класс формы, чтобы сослаться на неё во view-классе
from .forms import CreationForm
from django.contrib.auth.decorators import login_required

from urllib import response





def user_only(func):
    def check_user(request, *args, **kwargs):
        # Мы знаем, что у view-функций первый аргумент всегда request
        if not request.user.is_authenticated():
            return response.redirect(
                to_page = '/auth/login', 
                params = {'next': current_page} 
            )
        func(request, *args, **kwargs)
    return check_user