# Generated by Django 5.1.7 on 2025-03-07 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='defulat.jpg', upload_to='profile_pics'),
        ),
    ]
