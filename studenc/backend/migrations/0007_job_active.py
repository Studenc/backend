# Generated by Django 4.0.4 on 2022-05-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_apiaccesskey'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]