# Generated by Django 4.1 on 2022-08-21 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('endereco', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('unidade', models.CharField(max_length=2)),
                ('qtde_produto', models.DecimalField(decimal_places=2, max_digits=8)),
                ('estoque_max', models.DecimalField(decimal_places=2, max_digits=8)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('validade', models.DateField()),
                ('observacao', models.CharField(blank=True, max_length=140, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.categoria')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Movimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('qtde_movimento', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data', models.DateField()),
                ('observacao', models.CharField(blank=True, max_length=140, null=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
    ]
