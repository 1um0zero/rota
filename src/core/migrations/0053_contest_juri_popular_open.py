# Generated by Django 2.2 on 2020-11-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0052_auto_20201123_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='juri_popular_open',
            field=models.BooleanField(default=False),
        ),
    ]