# Generated by Django 4.0.4 on 2022-05-23 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0007_alter_coachingstaff_birthday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Players',
            new_name='Player',
        ),
        migrations.AlterModelOptions(
            name='player',
            options={'verbose_name_plural': 'player'},
        ),
    ]
