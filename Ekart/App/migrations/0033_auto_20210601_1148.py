# Generated by Django 3.0 on 2021-06-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0032_auto_20210601_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='cvv',
            field=models.IntegerField(max_length=20, null='True'),
        ),
    ]
