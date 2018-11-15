# Generated by Django 2.1.3 on 2018-11-15 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0006_auto_20181115_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Game'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Role'),
        ),
    ]
