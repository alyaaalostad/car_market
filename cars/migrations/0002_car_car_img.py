# Generated by Django 2.1.5 on 2019-08-26 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='car_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
