from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
        title = forms.CharField()
        text = forms.CharField()
        author = forms.CharField()
        

        class Meta:
            model = Article
            fields = [
                'title',
                'text',
                'author'
            ]
