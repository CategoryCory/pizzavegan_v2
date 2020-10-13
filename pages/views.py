from django.shortcuts import render, redirect
from django.contrib import messages

from contacts.forms import SurveyResponseForm


def homepage_view(request):
    if request.method == 'POST':
        form = SurveyResponseForm(request.POST)

        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Thank you for signing up! We will let you know when we officially launch!'
            )
            return redirect('pages:home')
        else:
            messages.add_message(
                request,
                messages.ERROR,
                'There was a problem signing up. Please try again later.'
            )
            return redirect('pages:home')
    else:
        form = SurveyResponseForm()

    context = {
        'form': form,
    }

    return render(request, 'pages/home.html', context)
