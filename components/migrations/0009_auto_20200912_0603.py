# Generated by Django 3.0.8 on 2020-09-12 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0008_component_reference_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='reference_id',
            field=models.CharField(max_length=250),
        ),
    ]
