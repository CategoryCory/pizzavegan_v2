from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    # path('new/', ArticleCreateView.as_view(), name='article_create'),
    # path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
]
