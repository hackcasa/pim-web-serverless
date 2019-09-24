# Generated by Django 2.1.1 on 2019-02-14 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0038_merge_20190214_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproduct',
            name='product_id',
            field=models.BigIntegerField(db_index=True, default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_id',
            field=models.BigIntegerField(default=0, unique=True),
        ),
    ]
