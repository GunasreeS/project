# Generated by Django 3.0 on 2021-05-27 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_auto_20210526_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='rolerest',
            name='email',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
