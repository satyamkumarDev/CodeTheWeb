# Generated by Django 3.0.5 on 2020-05-04 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.TextField(default='', max_length=150),
            preserve_default=False,
        ),
    ]
