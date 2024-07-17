# Generated by Django 5.0.6 on 2024-07-12 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField(default=2000)),
                ('genre', models.CharField(max_length=50)),
                ('rating', models.FloatField(default=0.0)),
                ('runtime', models.IntegerField(default=0)),
                ('review', models.TextField()),
                ('director', models.CharField(max_length=100)),
                ('actors', models.CharField(max_length=200)),
                ('image_url', models.URLField(max_length=2000)),
            ],
        ),
    ]
