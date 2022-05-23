from django.urls import path, re_path
from .views import Players, contracts, players_re, detail, index, GreetingView

urlpatterns = [
    path('', index),
    path('players/', Players.as_view()),
    path('players/<int:id>/', contracts),
    path('players/<int:id>/<slug:slug>', contracts),
    path('myview/<int:poll_id>', detail),
    re_path(r"^players-re/$", players_re),
    path('test', GreetingView.as_view(greeting='Salom'))
]
