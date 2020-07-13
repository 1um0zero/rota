# Generated by Django 2.2 on 2019-06-01 20:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190601_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='ddd',
            field=models.CharField(default=21, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 17, 37, 15, 621159)),
        ),
        migrations.AlterField(
            model_name='passwordrecoverytoken',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 17, 37, 15, 619581)),
        ),
        migrations.AlterField(
            model_name='script',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 17, 37, 15, 620619)),
        ),
        migrations.AlterField(
            model_name='short',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 17, 37, 15, 620178)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 1, 17, 37, 15, 618494)),
        ),
    ]
