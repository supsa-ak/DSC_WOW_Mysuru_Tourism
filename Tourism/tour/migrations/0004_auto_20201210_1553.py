# Generated by Django 3.1.1 on 2020-12-10 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0003_auto_20201210_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
