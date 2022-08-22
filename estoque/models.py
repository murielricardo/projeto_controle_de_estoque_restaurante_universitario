from django.db import models


class Categoria(models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.nome


UNIDADE_CHOICES = (
    ("Un", "Un"),
    ("Kg", "Kg"),
    ("g", "g"),
    ("Lt", "Lt"),
    ("ml", "ml"),
)


class Produto(models.Model):
    descricao = models.CharField(max_length=100)
    unidade = models.CharField(max_length=2, choices=UNIDADE_CHOICES)
    qtde_produto = models.DecimalField(decimal_places=2, max_digits=8)
    estoque_min = models.DecimalField(decimal_places=2, max_digits=8)
    preco = models.DecimalField(decimal_places=2, max_digits=8)
    validade = models.DateField()
    observacao = models.CharField(max_length=140, blank=True, null=True)
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


MOVIMENTO_CHOICES = (
    ("Entrada", "Entrada"),
    ("Saída", "Saída"),
)


class Movimento(models.Model):
    descricao = models.CharField(max_length=7, choices=MOVIMENTO_CHOICES)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    qtde_movimento = models.DecimalField(decimal_places=2, max_digits=8)
    data = models.DateField()
    observacao = models.CharField(max_length=140, blank=True, null=True)
