from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('create-new-article/', ArticleCreateView.as_view(), name='article_create'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<slug:slug>/edit/', ArticleUpdateView.as_view(), name='article_update'),
]
