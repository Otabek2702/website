from django.contrib import admin
from .models import Players, Contracts, CoachingStaff, ClubManagment

# Register your models here.

admin.site.register(ClubManagment)
admin.site.register(CoachingStaff)
admin.site.register(Players)
admin.site.register(Contracts)
