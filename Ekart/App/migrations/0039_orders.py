# Generated by Django 3.0 on 2021-06-03 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0038_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=300)),
                ('price', models.IntegerField()),
                ('im', models.ImageField(upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True, null='True')),
                ('prod', models.IntegerField(null=True)),
            ],
        ),
    ]
