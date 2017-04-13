from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, LargeBinary, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('mysql+pymysql://root:Oigul9Bluj1@localhost/checkupdate_db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

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

    atributos = [nome, baia, categoria, resp, serial, fabricante, modelo, localizacao,
                rack, patrimonio, hostname, ip, em_uso, said, contrato, start_date, end_date,
                leg_prod ]
