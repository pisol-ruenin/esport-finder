# Generated by Django 2.1.3 on 2018-11-15 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20181115_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='game',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='province',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]