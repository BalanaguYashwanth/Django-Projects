# Generated by Django 3.0.8 on 2020-08-28 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20200827_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo_data',
            name='confirm',
        ),
        migrations.RemoveField(
            model_name='todo_data',
            name='message',
        ),
    ]
