# Generated by Django 4.1 on 2022-10-05 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialMedia', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='media/ImgProfile/no-profile-photo.png', null=True, upload_to='ImgProfile'),
        ),
    ]