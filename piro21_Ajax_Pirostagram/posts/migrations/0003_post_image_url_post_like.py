# Generated by Django 5.0.7 on 2024-07-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.URLField(default='https://example.com/default-image.jpg'),
        ),
        migrations.AddField(
            model_name='post',
            name='like',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
