from pydantic import BaseModel


# ----------------------------------- Monitor ---------------------------------------------------


class MonitorCriar(BaseModel):
    nome : str
    polegadas : float
    frequencia : int
    preco : float


class MonitorEditar(BaseModel):
    nome : str
    polegadas : int
    frequencia : int
    preco : float


# ----------------------------------- Notebook ---------------------------------------------------


class NotebookCriar(BaseModel):
    nome : str
    polegadas : float
    quantidade_ram : int
    processador : str
    placa_video : str
    rgb : bool
    peso : float
    ssd : bool
    preco : float


class NotebookEditar(BaseModel):
    nome : str
    polegadas : float
    quantidade_ram : int
    processador : str
    placa_video : str
    rgb : bool
    peso : float
    ssd : bool
    preco : float


# ----------------------------------- Teclado ---------------------------------------------------

class TecladoCriar(BaseModel):
    nome : str
    modelo : str
    tipo_conexao : str
    cor : str
    preco : float


class TecladoEditar(BaseModel):
    nome : str
    modelo : str
    tipo_conexao : str
    cor  : str
    preco : float


# ----------------------------------- Mouse ---------------------------------------------------


class MouseCriar(BaseModel):
    nome : str
    dpi : int
    modelo : str
    rgb : bool
    quantidade_botao : int
    preco : float


class MouseEditar(BaseModel):
    nome : str
    dpi : int
    modelo : str
    rgb : bool
    quantidade_botao : int
    preco : float


# ----------------------------------- Combos 20% (Teclado e Mouse) ---------------------------------------------------


class Combo20Criar(BaseModel):
    nome_combo : str
    id_mouse: int
    id_teclado: int


class Combo20Editar(BaseModel):
    nome_combo : str
    id_mouse: int
    id_teclado: int