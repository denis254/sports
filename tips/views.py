from django.shortcuts import render, redirect
from . models import FreeTipsGame, VipTipsGame, RollTipsGame, PunterTipsGame
from django.utils import timezone
from . forms import RegistrationForm
from django.contrib.auth.decorators import login_required

def play(request):
    return redirect("https://play.google.com/store/apps/details?id=com.a1xpredict.a1xpredict")

@login_required()
def vipTips(request):

    model = FreeTipsGame

    template_name = 'vipTips.html'

    args = {}

    home_page_teams = VipTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, "vipTips/vip.html", args)

@login_required()
def punter(request):

    model = FreeTipsGame

    template_name = 'punter.html'

    args = {}

    home_page_teams = PunterTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, "vipTips/punter.html", args)

@login_required()
def roll(request):

    model = FreeTipsGame

    template_name = 'roll.html'

    args = {}

    home_page_teams = RollTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, "vipTips/roll.html", args)

def home(request):

    model = FreeTipsGame

    template_name = 'freeTips.html'

    args = {}

    home_page_teams = FreeTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, "freeTips/home.html", args)

def results(request):

    model = FreeTipsGame

    template_name = 'results.html'

    args = {}

    home_page_teams = FreeTipsGame.objects.filter(
        date_added__lte=timezone.now()
    ).order_by('-date_added')

    args ['home_page_teams'] = home_page_teams

    return render(request, "freeTips/results.html", args)

def subscribe(request):

    return render(request, "freeTips/subscribe.html")

def information(request):

    return render(request, "register/information.html")

@login_required()
def viphome(request):

    return render(request, "vipTips/vip_home.html")

def register(request):

    if request.method == 'POST':

        form = RegistrationForm(request.POST)

        if form.is_valid():

            user = form.save()

            user.save()

            return redirect('/information/')

    else:
        form = RegistrationForm()


    return render(request, 'register/register.html', {'form':form})
