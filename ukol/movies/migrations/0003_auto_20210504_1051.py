# Generated by Django 3.2 on 2021-05-04 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20210504_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='fname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='sname',
            new_name='surname',
        ),
    ]
