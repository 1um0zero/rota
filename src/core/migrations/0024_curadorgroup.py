# Generated by Django 2.2 on 2019-07-14 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20190711_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='CuradorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
    ]
