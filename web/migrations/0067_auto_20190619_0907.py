# Generated by Django 2.2.1 on 2019-06-19 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0066_auto_20190619_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='net_content',
            field=models.CharField(max_length=100, null=True, verbose_name='Net Content'),
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='net_content_unit_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Net Content Unit Code'),
        ),
        migrations.AddField(
            model_name='product',
            name='net_content',
            field=models.CharField(max_length=100, null=True, verbose_name='Net Content'),
        ),
        migrations.AddField(
            model_name='product',
            name='net_content_unit_code',
            field=models.CharField(max_length=10, null=True, verbose_name='Net Content Unit Code'),
        ),
    ]
