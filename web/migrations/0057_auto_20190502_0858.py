# Generated by Django 2.2 on 2019-05-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0056_auto_20190418_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='storage_temperature_range',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Storage Temperature Range'),
        ),
        migrations.AddField(
            model_name='article',
            name='storage_type',
            field=models.CharField(choices=[('Colonial', 'Colonial'), ('Refrigerated', 'Refrigerated'), ('Frozen', 'Frozen'), ('Unspecified', 'Unspecified')], default='Unspecified', max_length=64, verbose_name='Storage Type'),
        ),
        migrations.AddField(
            model_name='historicalarticle',
            name='storage_temperature_range',
            field=models.CharField(blank=True, default='', max_length=64, verbose_name='Storage Temperature Range'),
        ),
        migrations.AddField(
            model_name='historicalarticle',
            name='storage_type',
            field=models.CharField(choices=[('Colonial', 'Colonial'), ('Refrigerated', 'Refrigerated'), ('Frozen', 'Frozen'), ('Unspecified', 'Unspecified')], default='Unspecified', max_length=64, verbose_name='Storage Type'),
        ),
    ]
