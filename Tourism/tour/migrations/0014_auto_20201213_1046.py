# Generated by Django 3.1.4 on 2020-12-13 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0013_auto_20201213_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='valo',
            name='fieldname',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Images/'),
        ),
    ]
