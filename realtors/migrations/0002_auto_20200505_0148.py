# Generated by Django 3.0.5 on 2020-05-05 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/'),
        ),
    ]
