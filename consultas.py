from datetime import date

from peewee import PostgresqlDatabase, fn

from esquema import Categoria, Cliente, HistoricoPrecos, Produto, Venda

# Conectar ao banco de dados
db = PostgresqlDatabase('loja_peewee', port=5432,
                        user='postgres', password='06012002', host='localhost')
db.connect()

try:
    # Consulta 1: Histórico de preços de um produto específico
    print("Executando consulta 1...")
    produto = Produto.select().where(
        Produto.descricao == 'Caneta Bic esferográfica azul').get()
    historico_precos = HistoricoPrecos.select().where(
        HistoricoPrecos.produto == produto)
    for preco in historico_precos:
        print(f'Produto: {produto.descricao}, Preço: {
              preco.valor}, Data: {preco.data}')

    # Consulta 2: Produtos de uma categoria específica ordenados por preço
    print("\nExecutando consulta 2...")
    categoria = Categoria.select().where(Categoria.descricao == 'Papelaria').get()
    produtos = Produto.select().where(
        Produto.categoria == categoria).order_by(Produto.valor)
    for produto in produtos:
        print(f'Descrição: {produto.descricao}, Preço: {produto.valor}')

    # Consulta 3: Clientes com vendas acima de R$ 5000 em setembro de 2022
    print("\nExecutando consulta 3...")
    clientes = (Cliente
                .select()
                .join(Venda)
                .where((Venda.valor_total > 5000) &
                       (Venda.data.year == 2022) &
                       (Venda.data.month == 9))
                .group_by(Cliente)
                .order_by(fn.Lower(Cliente.nome)))

    # Contagem de clientes retornados
    num_clientes = clientes.count()
    print(f"Total de Clientes: {num_clientes}")

    for cliente in clientes:
        print(f'Nome do Cliente: {cliente.nome}')

except Exception as e:
    print(f"Erro ao executar consultas: {e}")

finally:
    # Fechar a conexão com o banco de dados
    if not db.is_closed():
        db.close()
