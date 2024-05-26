# Generated by Django 5.0.4 on 2024-05-02 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0008_alter_usuario_estado_civil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado_civil',
            field=models.CharField(choices=[('solteiro', 'solteiro'), ('casado', 'casado'), ('divorciado', 'divorciado'), ('separado', 'separado'), ('viuvo', 'viuvo')], default='selecione', max_length=20),
        ),
    ]
