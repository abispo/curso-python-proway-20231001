# Generated by Django 5.0.1 on 2024-02-11 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dados', '0004_remove_partida_data_remove_partida_hora_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clube',
            name='escudo',
            field=models.CharField(default='generico.svg', max_length=100),
        ),
    ]
