from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from . import models, forms


class ArticleListView(ListView):

    model = models.Article


class ArticleDetailView(DetailView):

    model = models.Article


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = models.Article
    form_class = forms.CreateArticleForm
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
