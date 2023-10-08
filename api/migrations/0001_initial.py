# Generated by Django 4.2.6 on 2023-10-08 18:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search_Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.CharField(max_length=255)),
                ('count', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
        migrations.CreateModel(
            name='Search_Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=100, null=True)),
                ('author', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('size', models.CharField(max_length=20)),
                ('extension', models.CharField(max_length=10)),
                ('link', models.URLField()),
                ('md5_id', models.CharField(max_length=32, unique=True)),
                ('uniqueId', models.CharField(blank=True, max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, max_length=500, null=True, unique=True)),
                ('date_created', models.DateTimeField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(blank=True, null=True)),
                ('searchquery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='searchFnt', to='api.search_query')),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]