# Generated by Django 4.2.2 on 2023-06-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitors', '0004_alter_booking_check_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='check_out',
            field=models.DateField(default='11/06/2023'),
        ),
    ]