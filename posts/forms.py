from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from posts.models import Post


User = get_user_model()


#  создадим собственный класс для формы регистрации
#  сделаем его наследником предустановленного класса UserCreationForm
class CreationForm(UserCreationForm):
    # он унаследован от родительских классов. В нём настраивается форма, 
    # и именно в нём мы переопределяем некоторые её параметры.
    class Meta(UserCreationForm.Meta):  # наследуется не основной класс,
        # а вложенный укажем модель, с которой связана создаваемая форма
        model = User
        # укажем, какие поля должны быть видны в форме и в каком порядке
        fields = ("first_name", "last_name", "username", "email")


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("group", "text")
