# Generated by Django 3.0.6 on 2020-06-25 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filex', '0009_auto_20200625_0632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesdata',
            name='myfile',
        ),
    ]
