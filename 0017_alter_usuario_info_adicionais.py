# Generated by Django 5.0.4 on 2024-05-03 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_cad_usuarios', '0016_usuario_info_adicionais'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='info_adicionais',
            field=models.TextField(blank=True, max_length=512, null=True),
        ),
    ]