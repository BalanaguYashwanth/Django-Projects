# Generated by Django 3.0.8 on 2020-08-07 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_filedata_fid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedata',
            name='picture',
            field=models.FileField(null=True, upload_to='photos/'),
        ),
    ]
