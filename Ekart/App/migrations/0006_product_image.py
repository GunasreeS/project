# Generated by Django 3.0 on 2021-05-12 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
