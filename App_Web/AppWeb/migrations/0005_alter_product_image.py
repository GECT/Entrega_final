# Generated by Django 4.2 on 2023-04-29 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0004_alter_wallpaper_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product'),
        ),
    ]
