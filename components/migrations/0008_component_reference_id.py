# Generated by Django 3.0.8 on 2020-09-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0007_customerdata_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='reference_id',
            field=models.IntegerField(default=1212),
            preserve_default=False,
        ),
    ]
