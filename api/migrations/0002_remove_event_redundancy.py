# Generated by Django 3.0.7 on 2021-06-20 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='krdetailsview',
            name='event',
        ),
        migrations.RemoveField(
            model_name='krtransaction',
            name='event',
        ),
    ]
