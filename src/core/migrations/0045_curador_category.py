# Generated by Django 2.2 on 2020-07-30 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20200728_1948'),
    ]

    operations = [
        migrations.AddField(
            model_name='curador',
            name='category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
