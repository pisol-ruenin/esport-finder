# Generated by Django 2.1.3 on 2018-11-15 19:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0010_auto_20181116_0011'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='followed',
            new_name='following',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together={('follower', 'following')},
        ),
    ]