# Generated by Django 3.1.7 on 2021-03-08 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0005_auto_20210307_2239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='date_added',
        ),
    ]