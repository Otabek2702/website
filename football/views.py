from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView
from .models import Player, Contracts

from .Football_club import models


# Create your views here.
class Index(ListView):
    model = Player
    template_name = 'football/player_list.html'
    context_object_name = 'players_list'


class ContractPlayerView(ListView):
    template_name = 'football/player_by_contracts.html'
    context_object_name = 'contracts'

    def get_queryset(self):
        self.contract = get_object_or_404(Player, id=self.kwargs['contract'])
        return Contracts.objects.filter(contract_id=self.contract)


class PlayerCreateView(CreateView):
    model = Player
    fields = ['name', 'surname', 'player_number', 'birthday_date', 'height', 'weight']
    template_name = 'football/create_player.html'


class PlayerUpdateView(UpdateView):
    model = Player
    template_name = 'football/update_player.html'
    fields = ['name', 'surname', 'player_number', 'birthday_date', 'height', 'weight', 'image']

    success_url = '/players'


class PlayersView(View):
    def get(self, request):
        print(request.GET)
        if 'f_name' in request.GET:
            searched_text = request.GET['f_name']
            print(searched_text)
            html = ''
            for item in models.Player.objects():
                if searched_text.lower() in item.name.lower():
                    html += f"<a href={item.id}>{item.name} {item.surname}</a><br>"
            return HttpResponse(html)
        else:
            return render(request, 'football/index.html', context={'players': Player.objects.all()})

    def post(self, request):
        print(self.request)
        return HttpResponse('asd')


def contracts(request, id=None, slug=None):
    html = ''
    if slug is not None:
        return HttpResponse(slug)
    if id is not None:
        for item in models.Contract.objects():
            if item.id == int(id):
                html += f"<img src='https://cdn.givemesport.com/wp-content/uploads/2022/03/GettyImages-1347865563" \
                        f"-1200x1200-c-default.jpg' alt='TerStegen' height=200 width=200><br><h1>Salary: {item.salary}" \
                        f"</h1"f"><br> "
                return HttpResponse(html, status=200)
    return HttpResponse(html, status=404)


def players_re(request):
    print(request.GET)
    s = ""
    for item in request.GET:
        s += f"{item} = {request.GET.get(item)}<br>"
    return HttpResponse(request.content_type)


def detail(request, poll_id):
    if poll_id:
        print(1)
    else:
        return Http404("Poll does not exist")
    return HttpResponse(request.GET)


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


class MorningGreetingView(GreetingView):
    greeting = "Morning to ya"
