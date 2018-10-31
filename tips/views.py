from django.shortcuts import render, redirect
from . models import FreeTipsGame, vipTipsGame, punterTipsGame
from django.utils import timezone
from . forms import RegistrationForm
from django.contrib import messages

#Today's Free tips method
def home(request):

    model = FreeTipsGame

    template_name = 'home.html'

    args = {}

    home_page_teams = FreeTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/home.html', args)

#Free tips results method
def results(request):

    model = FreeTipsGame

    template_name = 'free/results.html'

    args = {}

    home_page_teams = FreeTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/results.html', args)

def payment(request):
    return render(request, 'free/payment.html')

def viptips(request):
    return render(request, 'free/viptips.html')

def signup(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.save()

            messages.success(request, 'Registration successful.You can now log in with your username and password')

            return redirect('/accounts/login')

    else:
        form = RegistrationForm()


    return render(request, 'free/signup.html', {'form':form})

def viptipsgames(request):

    model = vipTipsGame

    template_name = 'viptipsgames.html'

    args = {}

    home_page_teams = vipTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/viptipsgames.html', args)

def punterpick(request):

    model = punterTipsGame

    template_name = 'punterpick.html'

    args = {}

    home_page_teams = punterTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, 'free/punterpick.html', args)
