# Generated by Django 5.0.6 on 2024-07-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='kindof',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='tool',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
