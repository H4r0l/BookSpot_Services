# Generated by Django 4.2.6 on 2023-10-26 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('published_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('isbn', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('rating', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(max_length=50)),
                ('length', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('book', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.book')),
                ('movie', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]