# Generated by Django 5.0.1 on 2024-01-19 18:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topico', '0004_alter_comentario_topico'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentario',
            name='topico',
        ),
        migrations.RemoveField(
            model_name='topico',
            name='conteudo',
        ),
        migrations.CreateModel(
            name='Postagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('topico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topico.topico')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='postagem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='topico.postagem'),
            preserve_default=False,
        ),
    ]
