from django import forms
from tinymce.widgets import TinyMCE

from .models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'slug', 'body', 'featured_image', 'status', ]
        widgets = {
            'body': TinyMCE(attrs={'cols': 25, 'rows': 10}),
        }
