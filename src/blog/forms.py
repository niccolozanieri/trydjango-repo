from django import forms
from .models import Article


class CreateArticleForm(forms.ModelForm):
    author = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'placeholder': "Insert you name...",
                'max_length': 40
            }
        )
    )

    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': "Fill this shit...",
                'max_length': 40
            }
        )
    )

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': "Write here...",
                'rows': 15
            }
        )
    )

    class Meta:
        model = Article
        fields = [
            'author',
            'title',
            'text'
        ]
