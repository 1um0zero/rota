# Generated by Django 2.2 on 2021-02-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_auto_20201124_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seminario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2048)),
                ('date', models.DateTimeField()),
                ('decription', models.TextField(null=True)),
            ],
        ),
    ]