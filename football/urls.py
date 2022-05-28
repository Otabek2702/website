from django.urls import path, re_path
from .views import PlayersView, contracts, players_re, detail, Index, GreetingView, ContractPlayerView, \
    PlayerCreateView, PlayerUpdateView

urlpatterns = [
    path('', Index.as_view()),
    path('players/', PlayersView.as_view()),
    path('players/create/', PlayerCreateView.as_view()),
    path('players/update/<int:pk>', PlayerUpdateView.as_view()),
    path('players/con/<contract>/', ContractPlayerView.as_view()),
    path('players/<int:id>/', contracts),
    path('players/<int:id>/<slug:slug>', contracts),
    path('myview/<int:poll_id>', detail),
    re_path(r"^players-re/$", players_re),
    path('test', GreetingView.as_view(greeting='Salom'))
]
