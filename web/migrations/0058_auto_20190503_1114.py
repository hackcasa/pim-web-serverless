# Generated by Django 2.1 on 2019-05-03 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0057_auto_20190502_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='vat',
            field=models.FloatField(default=0.0, verbose_name='VAT Rate'),
        ),
        migrations.AddField(
            model_name='product',
            name='vat',
            field=models.FloatField(default=0.0, verbose_name='VAT Rate'),
        ),
    ]
