# Generated by Django 5.0.4 on 2024-05-03 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0012_usuario_tipo_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_servico',
        ),
    ]
