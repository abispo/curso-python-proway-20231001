# Generated by Django 5.0.1 on 2024-02-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='bairro',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='cidade',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='logradouro',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='numero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tipo_logradouro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='uf',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]
