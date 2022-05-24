import datetime

from django.http import HttpResponse, Http404
# from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from .models import Player

from .Football_club import models


# Create your views here.
class Index(ListView):
    model = Player
    print('asd1')
    template_name = 'football/player_list.html'
    context_object_name = 'players_list'


class PlayersView(View):
    def get(self, request):
        print(request.GET)
        if 'f_name' in request.GET:
            searched_text = request.GET['f_name']
            print(searched_text)
            html = "<html><body>%s<h1 style=\"text-align: center\">Welcome to my page </h1></body></html><br>" \
                   % datetime.datetime.now()
            for item in models.Player.objects():
                if searched_text.lower() in item.name.lower():
                    html += f"<a href={item.id}>{item.name} {item.surname}</a><br>"
            return HttpResponse(html)
        else:
            html = "<html><body>%s<h1 style=\"text-align: center\">Welcome to my page </h1></body></html><br>" \
                   % datetime.datetime.now()
            for item in models.Player.objects():
                html = html + f"<a href=/players/{item.id}>{item.name} {item.surname}</a><br>"
            return HttpResponse(html, status=200)


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
