# Generated by Django 2.1 on 2019-01-04 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_remove_productcategory_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='metadescription',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='removed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
