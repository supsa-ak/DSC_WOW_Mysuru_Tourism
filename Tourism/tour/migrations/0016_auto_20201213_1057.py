# Generated by Django 3.1.4 on 2020-12-13 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0015_auto_20201213_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valo',
            name='doc',
            field=models.ImageField(default='', upload_to='Images'),
        ),
    ]
