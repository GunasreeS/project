# Generated by Django 3.0 on 2021-05-24 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0015_product_cid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='phonenu',
            field=models.IntegerField(null=True),
        ),
    ]
