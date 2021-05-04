# Generated by Django 3.2 on 2021-05-04 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('birth', models.DateField()),
                ('death', models.DateField(help_text='Leave empty if alive', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter studio name (e. g. Warner Bros. Pictures)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('release_year', models.PositiveIntegerField()),
                ('runtime', models.IntegerField()),
                ('score', models.IntegerField()),
                ('cast', models.ManyToManyField(to='movies.Actor')),
                ('directors', models.ManyToManyField(to='movies.Director')),
                ('genres', models.ManyToManyField(to='movies.Genre')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.studio')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='director',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.person'),
        ),
        migrations.AddField(
            model_name='director',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
        migrations.AddField(
            model_name='actor',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='movies.person'),
        ),
        migrations.AddField(
            model_name='actor',
            name='movies',
            field=models.ManyToManyField(to='movies.Movie'),
        ),
    ]
