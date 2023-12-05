from django.shortcuts import render, redirect
from .models import Band
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
import json
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    """
    View function for the home page of the site.

    :param request: HttpRequest object
    :return: HttpResponse with rendered home page template
    """
    return render(request, 'band/home.html')

def about(request):
    """
    View function for the about page of the site.

    :param request: HttpRequest object
    :return: HttpResponse with rendered about page template
    """
    return render(request, 'band/about.html')

@login_required
def band(request):
    """
    View function for the band listing page, accessible only by logged-in users.

    :param request: HttpRequest object
    :return: HttpResponse with rendered band page template
    """
    bands = Band.objects.all()
    return render(request, 'band/band.html',{'bands': bands})


def register(request):
    """
    View function for user registration.

    :param request: HttpRequest object
    :return: HttpResponse with rendered registration page template
    """
    try:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
                if user:
                    login(request, user)
                    return redirect('band')
                else:
                    return redirect('registration')

            else:
                return redirect('registration')
        else:
            form = UserCreationForm()
    except Exception as e:
        print(e)
    return render(request, 'registration/registration.html', {'form': form})



