# Generated by Django 2.2 on 2019-06-06 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20190605_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='data',
            field=models.TextField(null=True),
        ),
    ]
