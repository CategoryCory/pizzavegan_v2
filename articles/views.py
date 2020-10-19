from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models, forms


class ArticleListView(ListView):

    model = models.Article
    queryset = models.Article.objects.filter(status='published').order_by('-created_on')


class ArticleDetailView(DetailView):

    model = models.Article


class ArticleCreateView(LoginRequiredMixin, CreateView):

    model = models.Article
    form_class = forms.ArticleForm
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = models.Article
    form_class = forms.ArticleForm
    login_url = 'account_login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
