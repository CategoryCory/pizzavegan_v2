from django.urls import path

from .views import homepage_view, TapTheTableSignupView

app_name = 'pages'
urlpatterns = [
    path('', homepage_view, name='home'),
    path('register/', TapTheTableSignupView.as_view(), name='tap-the-table'),
]