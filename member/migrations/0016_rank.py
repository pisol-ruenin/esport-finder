# Generated by Django 2.1.3 on 2018-11-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_auto_20181118_0100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
        ),
    ]
