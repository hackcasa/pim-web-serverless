# Generated by Django 2.2.4 on 2019-09-22 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0074_auto_20190909_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='price',
            field=models.FloatField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='historicalarticle',
            name='price',
            field=models.FloatField(default=0, max_length=10),
        ),
    ]
