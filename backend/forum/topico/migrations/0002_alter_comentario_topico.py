# Generated by Django 5.0.1 on 2024-01-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topico', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='topico',
            field=models.ManyToManyField(blank=True, default=None, to='topico.topico'),
        ),
    ]
