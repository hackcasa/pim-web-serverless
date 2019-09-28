# Generated by Django 2.1.7 on 2019-03-06 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0046_auto_20190305_0945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='package_type',
        ),
        migrations.RemoveField(
            model_name='historicalarticle',
            name='package_type',
        ),
        migrations.AlterField(
            model_name='article',
            name='descriptor_code',
            field=models.CharField(choices=[('BASE_UNIT_OR_EACH', 'BASE_UNIT_OR_EACH'), ('CASE', 'CASE'), ('1/4', '1/4'), ('1/2', '1/2'), ('PALLET', 'PALLET')], max_length=64, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='article',
            name='vat',
            field=models.FloatField(choices=[(6.0, 6.0), (12.0, 12.0), (25.0, 25.0)], default=0, verbose_name='VAT'),
        ),
        migrations.AlterField(
            model_name='historicalarticle',
            name='descriptor_code',
            field=models.CharField(choices=[('BASE_UNIT_OR_EACH', 'BASE_UNIT_OR_EACH'), ('CASE', 'CASE'), ('1/4', '1/4'), ('1/2', '1/2'), ('PALLET', 'PALLET')], max_length=64, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='historicalarticle',
            name='vat',
            field=models.FloatField(choices=[(6.0, 6.0), (12.0, 12.0), (25.0, 25.0)], default=0, verbose_name='VAT'),
        ),
    ]
