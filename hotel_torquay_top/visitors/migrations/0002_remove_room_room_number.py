# Generated by Django 4.2.2 on 2023-06-10 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_number',
        ),
    ]