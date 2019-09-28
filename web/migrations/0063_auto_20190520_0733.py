# Generated by Django 2.2 on 2019-05-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0062_merge_20190507_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='last_receipt_day',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='last_sales_day',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='product_type',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Crossdocking', 'Crossdocking'), ('A', 'A')], default='Normal', max_length=128, verbose_name='Type'),
        ),
        migrations.AddField(
            model_name='product',
            name='last_receipt_day',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='last_sales_day',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Crossdocking', 'Crossdocking'), ('A', 'A')], default='Normal', max_length=128, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='historicalproduct',
            name='vat',
            field=models.FloatField(choices=[(0.0, 0.0), (6.0, 6.0), (12.0, 12.0), (25.0, 25.0)], default=0, verbose_name='VAT'),
        ),
        migrations.AlterField(
            model_name='product',
            name='vat',
            field=models.FloatField(choices=[(0.0, 0.0), (6.0, 6.0), (12.0, 12.0), (25.0, 25.0)], default=0, verbose_name='VAT'),
        ),
    ]
