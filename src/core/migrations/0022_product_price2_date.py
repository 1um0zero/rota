# Generated by Django 2.2 on 2019-07-11 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_product_price2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price2_date',
            field=models.DateField(default=None, null=True),
        ),
    ]
