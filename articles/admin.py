from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'status', 'created_on', ]
    list_editable = ['status', ]
    search_fields = ['title', 'body', ]
    list_per_page = 25
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
