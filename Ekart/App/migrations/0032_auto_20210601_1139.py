# Generated by Django 3.0 on 2021-06-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0031_delete_shippingaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='Expyear',
            field=models.CharField(max_length=20, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='creditcardnumber',
            field=models.IntegerField(null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='cvv',
            field=models.CharField(max_length=20, null='True'),
            preserve_default='True',
        ),
        migrations.AddField(
            model_name='user',
            name='expmonth',
            field=models.CharField(max_length=20, null='True'),
            preserve_default='True',
        ),
    ]
