# Generated by Django 3.0.8 on 2020-08-06 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20200716_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='filedata',
            name='fid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
