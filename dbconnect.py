from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, LargeBinary, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


home = '/home/ttosto_estag/Thiago/Projetos/Globosat/CheckUpdate3/'

with open(home + '.string_connection','r' ) as string:
	string_connection = string.read()
	

engine = create_engine(string_connection, echo=True, pool_recycle=30)
Base = declarative_base()
Session = sessionmaker(bind=engine)
dbsession = Session()

class Inventario(Base):
    __tablename__ = 'inventario'

    nome = Column(String)
    baia = Column(Integer)
    categoria = Column(String)
    resp = Column(String)
    serial = Column(String, primary_key=True)
    fabricante = Column(String)
    modelo = Column(String)
    localizacao = Column(String)
    rack = Column(Integer)
    patrimonio = Column(String)
    hostname = Column(String)
    ip = Column(String)
    em_uso = Column(String)
    said = Column(Integer)
    contrato = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    leg_prod = Column(String)
    posicao = Column(String)

    atributos = [nome, baia, categoria, resp, serial, fabricante, modelo, localizacao,
                rack, posicao, patrimonio, hostname, ip, em_uso, said, contrato, start_date, end_date,
                leg_prod]
