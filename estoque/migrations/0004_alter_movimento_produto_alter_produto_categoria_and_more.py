# Generated by Django 4.1 on 2022-08-22 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_alter_movimento_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimento',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estoque.produto'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estoque.categoria'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='estoque.fornecedor'),
        ),
    ]
