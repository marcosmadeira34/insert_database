from sqlalchemy import create_engine, Column, String, Integer, Date, inspect, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Index
from sqlalchemy.exc import IntegrityError
import pandas as pd


Base = declarative_base()

# classe para definir a tabela no banco de dados
class OrdersTable(Base):
    # nome da tabela no banco de dados
    __tablename__ = 'pedidosfaturados'
    
    # evita que dados duplicados sejam inseridos no banco de dados
    #__table_args__ = (UniqueConstraint('pedido_faturamento', 'id_equipamento'),)

    # colunas da tabela
    id = Column(Integer, primary_key=True, autoincrement='auto')
    codigo_cliente = Column(String, nullable=True, default="-")
    loja_cliente = Column(String, nullable=True, default="-")
    nome_do_cliente = Column(String, nullable=True, default="-")
    cnpj_do_cliente = Column(String, nullable=True, default="-")
    cnpj_de_faturamento = Column(String, nullable=True, default="-")
    cnpj_de_remessa = Column(String, nullable=True, default="-")
    equipamento = Column(String, nullable=True, default="-")
    nota_de_remessa = Column(String, nullable=True, default="-")
    data_de_remessa = Column(Date)
    serie_da_nf_remessa = Column(String, nullable=True, default="-")
    produto = Column(String, nullable=True, default="-")
    quantidade = Column(String, nullable=True, default="-")
    descricao_do_produto = Column(String, nullable=True, default="-")
    pedido_de_remessa = Column(String, nullable=True, default="-")
    projeto = Column(String, nullable=True, default="-")
    obra = Column(String, nullable=True, default="-")
    prazo_do_contrato = Column(String, nullable=True, default="-")
    data_de_ativacao_legado = Column(Date)
    data_de_ativacao = Column(Date)
    ultimo_faturamento = Column(Date)
    data_do_termo = Column(Date)
    aniversario = Column(Date)
    desc_ajuste = Column(String, nullable=True, default="-")
    indice_aplicado = Column(String, nullable=True, default="-")
    dias_de_locacao = Column(String, nullable=True, default="-")
    valor_de_origem = Column(String, nullable=True, default="-")
    valor_unitario = Column(String, nullable=True, default="-")
    valor_bruto = Column(String, nullable=True, default="-")
    tipo_do_mes = Column(String, nullable=True, default="-")
    contrato_legado = Column(String, nullable=True, default="-")
    acrescimo = Column(String, nullable=True, default="-")
    franquia = Column(String, nullable=True, default="-")
    id_equipamento = Column(String, nullable=True)
    id_equip_substituido = Column(String, nullable=True, default="-")
    data_da_substituicao = Column(Date)
    data_proximo_faturamento = Column(Date)
    data_fim_locacao = Column(Date)
    tipo_de_servico = Column(String, nullable=True, default="-")
    email = Column(String, nullable=True, default="-")
    calculo_reajuste = Column(String, nullable=True, default="-")
    nome_da_obra = Column(String, nullable=True, default="-")
    numero_da_as = Column(String, nullable=True, default="-")
    pedido_faturamento = Column(String, nullable=True, default="-")
    nf_de_faturamento = Column(String, nullable=True, default="-")
    serie_de_faturamento = Column(String, nullable=True, default="-")
    data_de_faturamento = Column(Date)
    qtde_faturamento = Column(String, nullable=True, default="-")
    vlr_unitario_faturamento = Column(String, nullable=True, default="-")
    vlr_total_faturamento = Column(String, nullable=True, default="-")
    periodo_de_faturamento = Column(String, nullable=True, default="-")
    status_de_cobranca = Column(String, nullable=True, default="-")

# classe para definir o nome da tabela no banco de dados    
class OrdersClass:
    def __init__(self, table_name):
        self.__table_name__ = table_name
        self.Table = OrdersTable


# classe para conexão com o banco de dados
class ConnectPostgresQL:
    # definindo construtor de classe com o parâmetros de conexão
    def __init__(self, host):
        self.engine = create_engine(host)
        
        self.Session = sessionmaker(bind=self.engine)
        

    # função para conexão com o banco de dados(PostgreSQL) self.engine.connect()
    def connect(self):
        return self.engine.connect()

    # função para criação do banco de dados e tabela
    def create_database(self):
        try:
            # inspeciona se a tabela existe no banco de dados
            inspector = inspect(self.engine)

            if not inspector.has_table(OrdersTable.__tablename__):
                Base.metadata.create_all(self.engine)
                print(f'Banco de Dados e Tabela {OrdersTable.__tablename__} criada com sucesso!')
            else:
                print(f'Dados já inseridos anteriormente na tabela {OrdersTable.__tablename__} !')
        except Exception as e:
            print(f'Erro ao criar banco de dados e tabel {OrdersTable.__tablename__}: {e}')


    # função para inserção de dados na tabela
    def insert_data(self, table_name, **kwargs):
        try:
            table = OrdersClass(table_name).Table

            with self.Session() as session:
                for key, value in kwargs.items():
                    if pd.isna(value) or isinstance(value, pd.Timestamp):
                        kwargs[key] = None
                    elif isinstance(value, str) and value == '-':
                        kwargs[key] = None
                    elif isinstance(value, str) and value == 'nan':
                        kwargs[key] = None
                    elif isinstance(value, str) and value == 'NaT':
                        kwargs[key] = None

                record = table(**kwargs)
                session.add(record)
                session.commit()
                #print(Fore.GREEN + f'Dados {key} inseridos com sucesso!' + Fore.RESET)
        # caso o registro já exista no banco de dados, não insere novamente
        except IntegrityError as e:
            pass

        # caso ocorra algum erro, exibe o erro    
        except Exception as e:
            raise e

        # fecha a conexão com o banco de dados
        finally:
            if session:
                session.close() 