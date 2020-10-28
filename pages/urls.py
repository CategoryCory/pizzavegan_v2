from django.urls import path

from .views import homepage_view, TapTheTableSignupView, AboutView

app_name = 'pages'
urlpatterns = [
    path('', homepage_view, name='home'),
    path('register/', TapTheTableSignupView.as_view(), name='tap-the-table'),
    path('about/', AboutView.as_view(), name='about'),
]