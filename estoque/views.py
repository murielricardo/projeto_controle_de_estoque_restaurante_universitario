from django.shortcuts import render, redirect
from estoque.forms import FornecedoresForm, ProdutosForm, CategoriasForm, MovimentacoesForm
from estoque.models import Fornecedor, Produto, Categoria, Movimento
from django.core.paginator import Paginator


def home(request):
    return render(request, 'home.html')


def dashboard(request):
    return render(request, 'dashboard.html')


# ----------------------------------------  INICIO FORNECEDORES ----------------------------------------------------
def fornecedores(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Fornecedor.objects.filter(nome__icontains=search)
    else:
        dados['db'] = Fornecedor.objects.all()

    return render(request, 'fornecedores_html/fornecedores.html', dados)


def form_fornecedores(request):
    data = {'form': FornecedoresForm()}
    return render(request, 'fornecedores_html/fornecedores_add.html', data)


def create_fornecedores(request):
    form = FornecedoresForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fornecedores')


def view_fornecedores(request, pk):
    data = {'db': Fornecedor.objects.get(pk=pk)}
    return render(request, 'fornecedores_html/fornecedores_view.html', data)


def fornecedores_edit(request):
    data = {'form': FornecedoresForm()}
    return render(request, 'fornecedores_html/fornecedores_edit.html', data)


def edit_fornecedores(request, pk):
    data = {'db': Fornecedor.objects.get(pk=pk)}
    data['form'] = FornecedoresForm(instance=data['db'])
    return render(request, 'fornecedores_html/fornecedores_edit.html', data)


def update_fornecedores(request, pk):
    data = {'db': Fornecedor.objects.get(pk=pk)}
    form = FornecedoresForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('fornecedores')


def delete_fornecedores(request, pk):
    db = Fornecedor.objects.get(pk=pk)
    db.delete()
    return redirect('fornecedores')


# ----------------------------------------  FIM FORNECEDORES ----------------------------------------------------


# ----------------------------------------  INICIO PRODUTOS -----------------------------------------------------

def produtos(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Produto.objects.filter(descricao__icontains=search)
    else:
        dados['db'] = Produto.objects.all()

    return render(request, 'produtos_html/produtos.html', dados)


def form_produtos(request):
    data = {'form': ProdutosForm()}
    return render(request, 'produtos_html/produtos_add.html', data)


def create_produtos(request):
    form = ProdutosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('produtos')


def view_produtos(request, pk):
    data = {'db': Produto.objects.get(pk=pk)}
    return render(request, 'produtos_html/produtos_view.html', data)


def produtos_edit(request):
    data = {'form': ProdutosForm()}
    return render(request, 'produtos_html/produtos_edit.html', data)


def edit_produtos(request, pk):
    data = {'db': Produto.objects.get(pk=pk)}
    data['form'] = ProdutosForm(instance=data['db'])
    return render(request, 'produtos_html/produtos_edit.html', data)


def update_produtos(request, pk):
    data = {'db': Produto.objects.get(pk=pk)}
    form = ProdutosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('produtos')


def delete_produtos(request, pk):
    db = Produto.objects.get(pk=pk)
    db.delete()
    return redirect('produtos')


# ----------------------------------------  FIM PRODUTOS ----------------------------------------------------------

# ----------------------------------------  INICIO CATEGORIAS -----------------------------------------------------

def categorias(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Categoria.objects.filter(descricao__icontains=search)
    else:
        dados['db'] = Categoria.objects.all()

    return render(request, 'categorias_html/categorias.html', dados)


def form_categorias(request):
    data = {'form': CategoriasForm()}
    return render(request, 'categorias_html/categorias_add.html', data)


def create_categorias(request):
    form = CategoriasForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('categorias')


def view_categorias(request, pk):
    data = {'db': Categoria.objects.get(pk=pk)}
    return render(request, 'categorias_html/categorias_view.html', data)


def produtos_categorias(request):
    data = {'form': CategoriasForm()}
    return render(request, 'categorias_html/categorias_edit.html', data)


def edit_categorias(request, pk):
    data = {'db': Categoria.objects.get(pk=pk)}
    data['form'] = CategoriasForm(instance=data['db'])
    return render(request, 'categorias_html/categorias_edit.html', data)


def update_categorias(request, pk):
    data = {'db': Categoria.objects.get(pk=pk)}
    form = CategoriasForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('categorias')


def delete_categorias(request, pk):
    db = Categoria.objects.get(pk=pk)
    db.delete()
    return redirect('categorias')


# ----------------------------------------  FIM CATEGORIAS -----------------------------------------------------------

# ----------------------------------------  INICIO MOVIMENTACOES -----------------------------------------------------

def movimentacoes(request):
    dados = {}
    search = request.GET.get('search')
    if search:
        dados['db'] = Movimento.objects.filter(descricao__icontains=search)
    else:
        dados['db'] = Movimento.objects.all()

    return render(request, 'movimentacoes_html/movimentacoes.html', dados)


def form_movimentacoes(request):
    data = {'form': MovimentacoesForm()}
    return render(request, 'movimentacoes_html/movimentacoes_add.html', data)


def create_movimentacoes(request):
    form = MovimentacoesForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movimentacoes')


def view_movimentacoes(request, pk):
    data = {'db': Movimento.objects.get(pk=pk)}
    return render(request, 'movimentacoes_html/movimentacoes_view.html', data)


def movimentacoes_edit(request):
    data = {'form': MovimentacoesForm()}
    return render(request, 'movimentacoes_html/movimentacoes_edit.html', data)


def edit_movimentacoes(request, pk):
    data = {'db': Movimento.objects.get(pk=pk)}
    data['form'] = MovimentacoesForm(instance=data['db'])
    return render(request, 'movimentacoes_html/movimentacoes_edit.html', data)


def update_movimentacoes(request, pk):
    data = {'db': Movimento.objects.get(pk=pk)}
    form = MovimentacoesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('movimentacoes')


def delete_movimentacoes(request, pk):
    db = Movimento.objects.get(pk=pk)
    db.delete()
    return redirect('movimentacoes')

# ----------------------------------------  FIM MOVIMENTACOES -----------------------------------------------------
