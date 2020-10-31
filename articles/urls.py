from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, RecipeListView, \
    RecipeDetailView

app_name = 'articles'
urlpatterns = [
    path('', ArticleListView.as_view(), name='articles_list'),
    path('create-new-article/', ArticleCreateView.as_view(), name='article_create'),
    path('article/<slug:slug>/', ArticleDetailView.as_view(), name='article_detail'),
    path('article/<slug:slug>/edit/', ArticleUpdateView.as_view(), name='article_update'),
    path('recipes/', RecipeListView.as_view(), name='recipes_list'),
    path('recipes/<slug:slug>/', RecipeDetailView.as_view(), name='recipe_detail'),
]
