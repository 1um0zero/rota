# Generated by Django 2.2 on 2021-02-12 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_seminario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seminario',
            old_name='decription',
            new_name='description',
        ),
    ]
