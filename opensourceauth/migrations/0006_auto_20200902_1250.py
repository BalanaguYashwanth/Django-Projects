# Generated by Django 3.0.8 on 2020-09-02 12:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opensourceauth', '0005_userbookings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbookings',
            old_name='driver_id',
            new_name='driverid',
        ),
    ]
