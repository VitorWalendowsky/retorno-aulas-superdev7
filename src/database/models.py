from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Double, String, Boolean, Numeric


Base = declarative_base()


# ------------------------------------------------ Monitor -------------------------------------------


class Monitor(Base):
    __tablename__= "monitores"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    polegadas = Column(Integer, nullable=False)
    frequencia = Column(Integer, nullable=False)
    preco = Column(Numeric(precision=10, scale=2), nullable=False)


# ------------------------------------------------ Notebook -------------------------------------------


class Notebook(Base):
    __tablename__ = "notebooks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    polegadas = Column(Numeric(precision=4, scale=1), nullable=False)
    quantidade_ram = Column(Integer, nullable=False)
    processador = Column(String(100), nullable=False)
    placa_video = Column(String(100), nullable=False)
    rgb = Column(Boolean, nullable=False)
    peso = Column(Numeric(precision=10, scale=2), nullable=False)
    ssd = Column(Boolean, nullable=False)
    preco = Column(Numeric(precision=10, scale=2), nullable=False)


# ------------------------------------------------ Teclado -------------------------------------------


class Teclado(Base):
    __tablename__ = "teclado"

    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(100), nullable=False)
    modelo = Column(String(100), nullable=False)
    tipo_conexao = Column(String(100), nullable=False)
    cor = Column(String(100), nullable=False)
    preco = Column(Numeric(precision=10, scale=2), nullable=False)


# ------------------------------------------------ Mouse -------------------------------------------


class Mouse(Base):
    __tablename__ = "mouse"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    dpi = Column(Integer, nullable=False)
    modelo = Column(String(100), nullable=False)
    rgb = Column(Boolean, nullable=False)
    quantidade_botao = Column(Integer, nullable=False)
    preco = Column(Numeric(precision=10, scale=2), nullable=False)