# Generated by Django 3.0 on 2021-05-27 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0026_rolerest_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolerest',
            name='cname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
