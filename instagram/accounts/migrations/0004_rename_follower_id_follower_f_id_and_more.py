# Generated by Django 5.0.6 on 2024-06-08 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_follower_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower_id',
            new_name='f_id',
        ),
        migrations.RenameField(
            model_name='following',
            old_name='follow_id',
            new_name='f_id',
        ),
    ]
