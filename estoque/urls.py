from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # -------------------------------------- FORNECEDORES --------------------------------------------
    path('fornecedores/', views.fornecedores, name='fornecedores'),
    path('form/fornecedores', views.form_fornecedores, name='form_fornecedores'),
    path('create/fornecedores/', views.create_fornecedores, name='create_fornecedores'),
    path('view/fornecedores/<int:pk>/', views.view_fornecedores, name='view_fornecedores'),
    path('edit/fornecedores/<int:pk>/', views.edit_fornecedores, name='edit_fornecedores'),
    path('update/fornecedores/<int:pk>/', views.update_fornecedores, name='update_fornecedores'),
    path('delete/fornecedores/<int:pk>/', views.delete_fornecedores, name='delete_fornecedores'),
    # -------------------------------------- PRODUTOS -----------------------------------------------
    path('produtos/', views.produtos, name='produtos'),
    path('form/produtos/', views.form_produtos, name='form_produtos'),
    path('create/produtos/', views.create_produtos, name='create_produtos'),
    path('view/produtos/<int:pk>/', views.view_produtos, name='view_produtos'),
    path('edit/produtos/<int:pk>/', views.edit_produtos, name='edit_produtos'),
    path('update/produtos/<int:pk>/', views.update_produtos, name='update_produtos'),
    path('delete/produtos/<int:pk>/', views.delete_produtos, name='delete_produtos'),
    # --------------------------------------- CATEGORIAS ---------------------------------------------
    path('categorias/', views.categorias, name='categorias'),
    path('form/categorias/', views.form_categorias, name='form_categorias'),
    path('create/categorias/', views.create_categorias, name='create_categorias'),
    path('view/categorias/<int:pk>/', views.view_categorias, name='view_categorias'),
    path('edit/categorias/<int:pk>/', views.edit_categorias, name='edit_categorias'),
    path('update/categorias/<int:pk>/', views.update_categorias, name='update_categorias'),
    path('delete/categorias/<int:pk>/', views.delete_categorias, name='delete_categorias'),
    # --------------------------------------- MOVIMENTAÇOES ---------------------------------------------
    path('movimentacoes/', views.movimentacoes, name='movimentacoes'),
    path('form/movimentacoes/', views.form_movimentacoes, name='form_movimentacoes'),
    path('create/movimentacoes/', views.create_movimentacoes, name='create_movimentacoes'),
    path('view/movimentacoes/<int:pk>/', views.view_movimentacoes, name='view_movimentacoes'),
    path('edit/movimentacoes/<int:pk>/', views.edit_movimentacoes, name='edit_movimentacoes'),
    path('update/movimentacoes/<int:pk>/', views.update_movimentacoes, name='update_movimentacoes'),
    path('delete/movimentacoes/<int:pk>/', views.delete_movimentacoes, name='delete_movimentacoes'),
]
