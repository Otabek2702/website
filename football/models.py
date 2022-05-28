from datetime import date
from django.db import models


# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    player_number = models.PositiveIntegerField(blank=True)
    birthday_date = models.DateField(default=date.today)
    height = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    image = models.ImageField(upload_to='media/players', null=True)

    class Meta:
        verbose_name_plural = "player"

    def __str__(self):
        return f'{self.name} {self.surname}'


class Contracts(models.Model):
    contract = models.OneToOneField(Player, on_delete=models.CASCADE, name='contract')
    validity = models.DateField(default=date.today)
    salary = models.FloatField(default=0)
    # signer_id = models.ForeignKey()

    class Meta:
        verbose_name_plural = 'contracts'

    def __str__(self):
        return f"{self.contract}"


class ClubManagment(models.Model):
    PRESTIGE = [
        ('Pr', 'Prezident'),
        ('V-Pr', 'Vitse-Prezident'),
        ('Ijro-Dir', 'Ijro-Direktori'),
        ('SD', 'Sport-Direktori')
    ]

    name_cm = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    nationalty = models.CharField(max_length=30)
    birthday_date = models.DateField()
    prestige = models.CharField(max_length=10, choices=PRESTIGE)

    class Meta:
        verbose_name_plural = "club_managment"

    def __str__(self):
        return f"{self.name_cm} {self.surname}"


class CoachingStaff(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    nationality = models.CharField(max_length=30)
    specialization = models.CharField(max_length=30)
    birthday = models.DateField(default=date.today)

    def __str__(self):
        return f"{self.name} {self.surname}"
