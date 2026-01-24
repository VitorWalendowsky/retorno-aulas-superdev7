from fastapi import Depends, FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

from classes import Combo20Criar, Combo20Editar, MouseCriar, MouseEditar, TecladoCriar, TecladoEditar
from src.database.conexao import get_db

from src.repositorios import combos_20_porcento_repositorio, produto_monitor_repositorio, produto_mouse_repositorio, produto_notebook_repositorio, produto_teclado_repositorio

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


@app.get("/api/v1/teclados/{id}")
def obter_teclado_por_id(id: int, db: Session = Depends(get_db)):
    teclado = produto_teclado_repositorio.obter_por_id(db, id)

    return teclado
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


@app.post("/api/v1/mouses")
def cadastrar_mouse(mouse: MouseCriar, db: Session = Depends(get_db)):
    mouse = produto_mouse_repositorio.cadastrar(
        db,
        mouse.nome,
        mouse.dpi,
        mouse.modelo,
        mouse.rgb,
        mouse.quantidade_botao,
        mouse.preco,
    )

    return mouse


@app.get("/api/v1/mouses")
def obter_mouses(db: Session = Depends(get_db)):
    mouses = produto_mouse_repositorio.obter_todos(db)

    return mouses


@app.get("/api/v1/mouses/{id}")
def obter_mouse_por_id(id: int, db: Session = Depends(get_db)):
    mouse = produto_mouse_repositorio.obter_por_id(db, id)
    
    if mouse == 0:
        raise HTTPException(status_code=404, detail="Mouse não encontrado.")
    

    return mouse


@app.delete("/api/v1/mouses/{id}")
def apagar_mouse(id: int, db: Session = Depends(get_db)):
    linhas_apagadas = produto_mouse_repositorio.apagar(db, id)

    if linhas_apagadas != 1:
        raise HTTPException(status_code=404, detail="Mouse não encontrado para apagar.")
    
    return {
        "status": "Mouse apagado com sucesso!"
    }


@app.put("/api/v1/mouses/{id}")
def editar_mouse(id: int, mouse: MouseEditar, db: Session = Depends(get_db)):
    linhas_alteradas = produto_mouse_repositorio.editar(db,
    id,
    mouse.nome,
    mouse.dpi,
    mouse.modelo,
    mouse.rgb,
    mouse.quantidade_botao,
    mouse.preco,
    )

    if linhas_alteradas != 1:
        raise HTTPException(status_code=404, detail="Mouse não encontrado para edição.")
    
    return {
        "status": "Mouse alterado com sucesso!"
    }


# ---------------------------------------------------------------------------------------------------------------------

# Possivel promoção 20%  - Mouse & Teclado (
# nome produto mouse = referencia Mouse
# preco original = preco Mouse
# preco final (desconto) = preco final após desconto
# nome produto mouse = referencia Teclado
# preco original = preco Teclado
# preco final (desconto) = preco final após desconto
# valor final compra = valor final da compra
# valor final desconto = valor do desconto 
# )

@app.get("/api/v1/combos_20_porcento")
def obter_todos_combos(db: Session = Depends(get_db)):
    promocoes = combos_20_porcento_repositorio.obter_todos(db)

    return promocoes


@app.post("/api/v1/combos_20_porcento")
def cadastrar_combo(combo: Combo20Criar, db: Session = Depends(get_db)):
    combo = combos_20_porcento_repositorio.cadastrar_combo(
        db,
        combo.nome_combo,
        combo.id_mouse,
        combo.id_teclado,
    )

    return combo


@app.put("/api/v1/combos_20_porcento/{id}")
def editar_combo(id: int, combo: Combo20Editar, db: Session = Depends(get_db)):
    combo = combos_20_porcento_repositorio.editar_combo(
        db,
        id,
        combo.nome_combo,
        combo.id_mouse,
        combo.id_teclado
    )

    if combo != 1:
        raise HTTPException(status_code=404, detail="Combo de Teclado e Mouse não encontrado para edição.")
    
    return {
        "status": "Combo modificado com sucesso!"
    }


@app.delete("/api/v1/combos_20_porcento/{id}")
def apagar_combo(id: int, db: Session = Depends(get_db)):
    linhas_apagadas = combos_20_porcento_repositorio.apagar_combo(db, id)

    if linhas_apagadas != 1:
        raise HTTPException(status_code= 404, detail="Não foi possível encontrar o combo para apagá-lo.")
    
    return {
        "status": "Combo deletado com sucesso!"
    }


@app.get("/api/v1/combos_20_porcento/{id}")
def obter_combo_por_id(id: int, db: Session = Depends(get_db)):
    combo = combos_20_porcento_repositorio.obter_combo_por_id(db, id)

    if combo == 0:
        raise HTTPException(status_code= 404, detail="Combo não encontrado.")
    
    return combo