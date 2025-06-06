# Generated by Django 5.2 on 2025-05-25 17:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('MediaList', '0001_initial'), ('MediaList', '0002_alter_media_cover')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MediaCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MediaProduction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor', models.JSONField(max_length=255)),
                ('director', models.CharField(max_length=255)),
                ('studio', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('synopsis', models.TextField()),
                ('release_date', models.DateField()),
                ('classification', models.CharField(choices=[('L', 'Livre para todos os públicos'), ('10', 'Não recomendado para menores de 10 anos'), ('12', 'Não recomendado para menores de 12 anos'), ('14', 'Não recomendado para menores de 14 anos'), ('16', 'Não recomendado para menores de 16 anos'), ('18', 'Não recomendado para menores de 18 anos')], max_length=50)),
                ('duration', models.IntegerField()),
                ('genres', models.CharField(max_length=125)),
                ('cover', models.ImageField(blank=True, null=True, upload_to='media_cover/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MediaList.mediacategory')),
                ('production', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='MediaList.mediaproduction')),
            ],
        ),
    ]
