# Generated by Django 3.0 on 2021-05-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0024_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=30, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='phno',
            field=models.CharField(max_length=30, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='pin',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(max_length=40, null='True'),
            preserve_default='True',
        ),
    ]
