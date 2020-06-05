from django import forms
from .models import Post

#PostForm é o nome do formulário
class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ('title','text')