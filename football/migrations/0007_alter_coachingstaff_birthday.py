# Generated by Django 4.0.4 on 2022-05-21 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0006_alter_clubmanagment_options_alter_contracts_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coachingstaff',
            name='birthday',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
