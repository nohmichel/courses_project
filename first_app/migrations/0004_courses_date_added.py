# Generated by Django 3.1.7 on 2021-03-08 05:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_auto_20210307_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
