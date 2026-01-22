from fastapi import Depends, FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from classes import TecladoCriar, TecladoEditar
from src.database.conexao import get_db

from src.repositorios import produto_monitor_repositorio, produto_mouse_repositorio, produto_notebook_repositorio, produto_teclado_repositorio

app = FastAPI()


# Teste

# 4 crus (2 por aluno)

#PeriPecas:
# - Monitor 
# 
# ( Nome ou Loja (Samsung / ASUS / etc..)
# - Tamanho x"
# - Frequencia Hz 
# - Preco R$)

# - Notebook 
# 
# ( Nome ou marca (Dell / Acer / etc..)
# - Tamanho Tela" 
# - Memoria RAM GB 
# - Preco R$ 
# - Loja
# - Processador 
# - placa de video 
# - marca da placa de video 
# - RGB S/N - peso kg 
# - SSD S/N)

# - Teclado 
# 
# ( Nome (Reddragon / Logitech / etc..)
# - Preco R$ 
# - modelo
# - Gamer ou Não(RGB)  
# - Conexão 
# - Cor)

@app.get("/api/v1/teclados")
def listar_teclados(db: Session = Depends(get_db)):
    teclados = produto_teclado_repositorio.obter_todos(db)

    return teclados


@app.post("/api/v1/teclados")
def cadastrar_teclado(teclado: TecladoCriar, db: Session = Depends(get_db)):
    teclado = produto_teclado_repositorio.cadastrar(
        db,
        teclado.nome,
        teclado.modelo,
        teclado.tipo_conexao,
        teclado.cor,
        teclado.preco,
    )

    return teclado


@app.delete("/api/v1/teclados/{id}")
def apagar_teclado(id: int, db: Session = Depends(get_db)):
    linhas_apagadas = produto_teclado_repositorio.apagar(db, id)

    if linhas_apagadas != 1:
        raise HTTPException(status_code=404, detail="Teclado não encontrado no sistema.")
    
    return {
        "status": "Apagado com sucesso."
    }


@app.put("/api/v1/teclados/{id}")
def editar_teclado(id: int, teclado: TecladoEditar, db: Session = Depends(get_db)):
    linhas_afetadas = produto_teclado_repositorio.editar(
        db,
        id,
        teclado.nome,
        teclado.modelo,
        teclado.tipo_conexao,
        teclado.cor,
        teclado.preco,
    )

    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="Teclado não encontrado.")
    
    return {
        "status": "Teclado alterado com sucesso."
    }
# ---------------------------------------------------------------------------------------------------------------------


# - Mouse 
# 
# ( Nome (Marca / Codenome)
# - Preco R$ 
# - modelo 
# - DPI 
# - Gamer ou Não(RGB) 
# - Quantidade de botão)

# pip install pymysql
# pip freeze > requirements.txt