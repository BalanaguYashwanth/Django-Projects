# Generated by Django 3.0.6 on 2020-06-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filex', '0005_auto_20200622_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='zone',
            new_name='email',
        ),
        migrations.AddField(
            model_name='details',
            name='phone',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='details',
            name='place',
            field=models.CharField(max_length=250),
        ),
    ]
