# Generated by Django 5.0.4 on 2024-05-06 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0023_alter_usuario_senha_gov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='senha_gov',
            field=models.CharField(default='valor_padrao', max_length=20),
        ),
    ]
