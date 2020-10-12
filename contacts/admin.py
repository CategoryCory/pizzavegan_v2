from django.contrib import admin

from .models import TapTheTableResponse, SurveyResponse


class TapTheTableResponseAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'email_address', 'facebook_page', 'is_subscriber', ]
    search_fields = ['restaurant_name', ]
    list_per_page = 25


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['email', 'pizza_description', ]


admin.site.register(TapTheTableResponse, TapTheTableResponseAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
