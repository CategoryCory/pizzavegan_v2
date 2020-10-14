from django import forms
# from tinymce.widgets import TinyMCE

from .models import Article


class CreateArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'slug', 'body', 'featured_image', 'featured_image_caption', 'status', ]
        widgets = {
            # 'body': TinyMCE(attrs={'cols': 25, 'rows': 3}),
        }
