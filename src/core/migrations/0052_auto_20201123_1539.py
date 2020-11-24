# Generated by Django 2.2 on 2020-11-23 18:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0051_juripopular_marcaencontro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juripopular',
            name='evaluator',
        ),
        migrations.AddField(
            model_name='juripopular',
            name='evaluators',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='juripopular',
            name='votes',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CategoriaJuriPopular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024)),
                ('contest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Contest')),
            ],
        ),
        migrations.AddField(
            model_name='juripopular',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.CategoriaJuriPopular'),
        ),
    ]
