# Generated by Django 5.0.6 on 2024-06-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='profilepic',
            field=models.ImageField(default='', upload_to='profile'),
            preserve_default=False,
        ),
    ]
