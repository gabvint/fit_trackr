# Generated by Django 4.2.16 on 2024-09-20 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_alter_meal_meal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='meal_goal',
        ),
    ]
