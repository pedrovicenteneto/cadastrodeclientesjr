# Generated by Django 5.0.4 on 2024-05-03 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0014_usuario_tipo_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='senha_gov',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
