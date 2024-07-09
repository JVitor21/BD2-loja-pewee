from peewee import*
db = PostgresqlDatabase('loja_peewee',port=5432,user='postgres',password='06012002',host='localhost')


class BaseModel(Model):
    class Meta:
        database = db

class Categoria(BaseModel):
    
    descricao = CharField()

class Cliente(BaseModel):
    
    nome = CharField()
    endereco = CharField()
    data_registro = DateField()

class Produto(BaseModel):
    id = AutoField(primary_key=True)
    descricao = CharField()
    categoria = ForeignKeyField(Categoria)
    valor = DecimalField()

class HistoricoPrecos(BaseModel):
  
    produto = ForeignKeyField(Produto)
    valor = DecimalField()
    data = DateField()

class Venda(BaseModel):
    
    produto = ForeignKeyField(Produto)
    cliente = ForeignKeyField(Cliente)
    data = DateField()
    quantidade = IntegerField()
    valor_unitario = DecimalField()
    valor_total = DecimalField()

db.connect()
db.create_tables([Categoria, Cliente, Produto, HistoricoPrecos, Venda])
