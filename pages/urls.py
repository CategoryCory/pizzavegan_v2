from django.urls import path

from .views import homepage_view, TapTheTableSignupView, AboutView, MeetEditorView, ContactUsView

app_name = 'pages'
urlpatterns = [
    path('', homepage_view, name='home'),
    path('register/', TapTheTableSignupView.as_view(), name='tap-the-table'),
    path('about/', AboutView.as_view(), name='about'),
    path('meet-the-editor/', MeetEditorView.as_view(), name='meet-the-editor'),
    path('contact/', ContactUsView.as_view(), name='contact_us'),
]