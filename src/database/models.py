from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, Double, String, Boolean, Numeric, ForeignKey


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

    combo_20_porcento = relationship("Combo_20_Porcento", back_populates="teclado")


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

    combo_20_porcento = relationship("Combo_20_Porcento", back_populates="mouse")

# ------------------------------------------------ Desconto -------------------------------------------


class Combo_20_Porcento(Base):
    __tablename__ = "combo_20_porcento"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_combo = Column(String(100), nullable=False)
    id_mouse = Column(Integer, ForeignKey("mouse.id"))
    id_teclado = Column(Integer, ForeignKey("teclado.id"))

    mouse = relationship("Mouse", back_populates="combo_20_porcento")

    teclado = relationship("Teclado", back_populates="combo_20_porcento")
    