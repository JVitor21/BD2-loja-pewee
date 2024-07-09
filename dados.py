from datetime import date
from peewee import *
from esquema import Categoria, Cliente, Produto, HistoricoPrecos, Venda

db = PostgresqlDatabase('loja_peewee', port=5432,user='postgres', password='06012002', host='localhost')

# Conectar ao banco de dados
db.connect()

# Criar tabelas se ainda não existirem
db.create_tables([Categoria, Cliente, Produto, HistoricoPrecos, Venda])

# Formate a data como uma string no formato 'YYYY-MM-DD'
data_formatada = date.today().strftime('%Y-%m-%d')

# Inserir dados nas tabelas
# Categorias
categoria1 = Categoria.create(descricao='Papelaria')
categoria2 = Categoria.create(descricao='Eletrônicos')

# Clientes
cliente1 = Cliente.create(
    nome='Cliente 1', endereco='Endereço 1', data_registro=data_formatada)
cliente2 = Cliente.create(
    nome='Cliente 2', endereco='Endereço 2', data_registro=data_formatada)

# Produtos
produto1 = Produto.create(
    descricao='Caneta Bic esferográfica azul', categoria=categoria1, valor=2.50)
produto2 = Produto.create(descricao='Notebook',
                          categoria=categoria2, valor=800.00)

# Histórico de Preços
HistoricoPrecos.create(produto=produto1, valor=2.50, data=data_formatada)
HistoricoPrecos.create(produto=produto2, valor=800.00, data=data_formatada)

# Vendas
Venda.create(produto=produto1, cliente=cliente1, data=data_formatada,
             quantidade=2, valor_unitario=2.50, valor_total=5.00)
Venda.create(produto=produto2, cliente=cliente2, data=data_formatada,
             quantidade=1, valor_unitario=800.00, valor_total=800.00)

# Inserir mais dados para teste
for _ in range(8):
    Venda.create(produto=produto1, cliente=cliente1, data=data_formatada,
                 quantidade=2, valor_unitario=2.50, valor_total=5.00)

for _ in range(9):
    Venda.create(produto=produto2, cliente=cliente2, data=data_formatada,
                 quantidade=1, valor_unitario=800.00, valor_total=800.00)

# Fechar a conexão com o banco de dados
db.close()
