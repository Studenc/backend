# Generated by Django 4.0.4 on 2022-05-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_company_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='code',
            field=models.IntegerField(unique=True),
        ),
    ]
