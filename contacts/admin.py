from django.contrib import admin

from .models import TapTheTableResponse, SurveyResponse, ContactUsResponse


class TapTheTableResponseAdmin(admin.ModelAdmin):
    list_display = ['restaurant_name', 'email_address', 'facebook_page', 'is_subscriber', 'is_approved', ]
    list_editable = ['is_approved', ]
    search_fields = ['restaurant_name', ]
    list_per_page = 25


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = ['email', 'pizza_description', ]


class ContactUsResponseAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', ]


admin.site.register(TapTheTableResponse, TapTheTableResponseAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(ContactUsResponse, ContactUsResponseAdmin)
