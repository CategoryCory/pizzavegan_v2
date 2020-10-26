from django.shortcuts import render
from django.views.generic import ListView, DetailView

from contacts.models import TapTheTableResponse


class PizzeriaList(ListView):

    model = TapTheTableResponse
    template_name = 'pizzerias/pizzeria_list.html'


class PizzeriaDetail(DetailView):

    model = TapTheTableResponse
    template_name = 'pizzerias/pizzeria_detail.html'
    context_object_name = 'pizzeria'
