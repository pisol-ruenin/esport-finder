# Generated by Django 2.1.3 on 2018-11-20 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0009_teamrecruitpost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamrecruitpost',
            name='img_cover',
        ),
    ]