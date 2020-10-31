from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.conf import settings

from contacts.models import TapTheTableResponse


class PizzeriaList(ListView):

    model = TapTheTableResponse
    template_name = 'pizzerias/pizzeria_list.html'
    queryset = TapTheTableResponse.objects.filter(is_approved=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_api_key'] = settings.MAPS_API_KEY
        return context


class PizzeriaDetail(DetailView):

    model = TapTheTableResponse
    template_name = 'pizzerias/pizzeria_detail.html'
    context_object_name = 'pizzeria'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['maps_api_key'] = settings.MAPS_API_KEY
        return context
