# Generated by Django 2.2 on 2019-06-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_subscription_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
