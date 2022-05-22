from django.urls import path, re_path
from .views import players, contracts, players_re, detail, index

urlpatterns = [
    path('', index),
    path('players/', players),
    path('players/<int:id>/', contracts),
    path('players/<int:id>/<slug:slug>', contracts),
    path('myview/<int:poll_id>', detail),
    re_path(r"^players-re/$", players_re)
]
