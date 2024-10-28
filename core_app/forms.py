from django import forms
from .models import Tag, Post
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'placeholder': "Введите имя пользователя"
        })
        self.fields['password'].widget.attrs.update({
            'placeholder': "Введите пароль"
        })

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Введите название тега',
                'class': 'input-tag'
            })
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'tag', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': "Введите название поста"
            }),
            'description': forms.Textarea(attrs={
                'placeholder': "Введите описание поста",
                'rows': 4
            })
        }