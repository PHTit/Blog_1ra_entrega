# Generated by Django 4.0.4 on 2022-06-06 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coder_course', '0006_remove_peliculas_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gastronomia',
            name='plot',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='libros',
            name='plot',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='peliculas',
            name='plot',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='viajes',
            name='plot',
            field=models.TextField(default=''),
        ),
    ]
