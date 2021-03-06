# Generated by Django 3.0.8 on 2020-09-23 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('components', '0014_component_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='component_name',
        ),
        migrations.RemoveField(
            model_name='component',
            name='description',
        ),
        migrations.RemoveField(
            model_name='component',
            name='percentage',
        ),
        migrations.RemoveField(
            model_name='component',
            name='reference_id',
        ),
        migrations.RemoveField(
            model_name='component',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='component',
            name='title',
        ),
        migrations.CreateModel(
            name='componentupdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_name', models.CharField(max_length=150)),
                ('customer_name', models.CharField(max_length=150)),
                ('purchase_order_no', models.CharField(max_length=150)),
                ('version', models.IntegerField()),
                ('Date_issued', models.CharField(max_length=150)),
                ('line_no', models.IntegerField()),
                ('qty', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('additional_information', models.TextField()),
                ('unit_weight', models.IntegerField()),
                ('total_weight', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('due_data', models.CharField(max_length=150)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('reference_id', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
