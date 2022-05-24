from django.contrib import admin
from .models import Player, Contracts, CoachingStaff, ClubManagment

# Register your models here.

admin.site.register(ClubManagment)
admin.site.register(CoachingStaff)
admin.site.register(Player)
admin.site.register(Contracts)
