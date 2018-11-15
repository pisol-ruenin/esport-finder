# Generated by Django 2.1.3 on 2018-11-15 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20181115_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Game'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='province',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Country'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='member.Role'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='cover_img',
            field=models.ImageField(blank=True, default='default/defult_cover.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, default='default/defult_profile.png', upload_to=''),
        ),
    ]
