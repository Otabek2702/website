# Generated by Django 4.0.4 on 2022-05-21 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_rename_contract_id_contracts_contract'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clubmanagment',
            options={'verbose_name_plural': 'club_managment'},
        ),
        migrations.AlterModelOptions(
            name='contracts',
            options={'verbose_name_plural': 'contracts'},
        ),
        migrations.AlterModelOptions(
            name='players',
            options={'verbose_name_plural': 'players'},
        ),
    ]
