# Generated by Django 2.1.1 on 2019-02-27 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0044_auto_20190225_1459'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='merchantarticle',
            options={'ordering': ['-id']},
        ),
        migrations.AddField(
            model_name='historicalproduct',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
