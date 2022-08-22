from django import forms
from estoque.models import Fornecedor, Categoria, Movimento
from estoque.models import Produto


class FornecedoresForm(forms.ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'endereco', 'email']

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }


class ProdutosForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'unidade', 'qtde_produto', 'estoque_min', 'preco', 'validade', 'observacao',
                  'fornecedor', 'categoria']

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'unidade': forms.Select(attrs={'class': 'form-control'}),
            'qtde_produto': forms.NumberInput(attrs={'class': 'form-control'}),
            'estoque_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'validade': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'observacao': forms.TextInput(attrs={'class': 'form-control'}),
            'fornecedor': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }


class CategoriasForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descricao']

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
        }


class MovimentacoesForm(forms.ModelForm):
    class Meta:
        model = Movimento
        fields = ['descricao', 'produto', 'qtde_movimento', 'data', 'observacao']

        widgets = {
            'descricao': forms.Select(attrs={'class': 'form-control', 'autofocus': ''}),
            'produto': forms.Select(attrs={'class': 'form-control'}),
            'qtde_movimento': forms.NumberInput(attrs={'class': 'form-control'}),
            'data': forms.SelectDateWidget(attrs={'class': 'form-control'}),
            'observacao': forms.TextInput(attrs={'class': 'form-control'})
        }
