# Generated by Django 3.2 on 2021-05-04 21:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0014_alter_movie_studio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='studio',
        ),
        migrations.DeleteModel(
            name='Studio',
        ),
    ]
