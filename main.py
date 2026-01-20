# Teste


# 4 crus (2 por aluno)

#Temas:
# - Monitor ( Tamanho x"- Frequencia Hz - Preco R$ - Loja)
# - Notebook ( Tamanho Tela" - Memoria RAM GB - Preco R$ - Loja - placa de video - marca da placa de video - RGB S/N - peso kg - SSD S/N)

from fastapi import Depends, FastAPI, HTTPException

from classes import AlunoCalcularMedia, CategoriaCriar, CategoriaEditar, ClienteCriar, ClienteEditar, ProdutoCriar, ProdutoEditar
from src.database.conexao import get_db
from src.database.models import Livro, Manga
from src.repositorios import livros_repositorio, manga_repositorio, mercado_categoria_repositorio, mercado_cliente_repositorio, mercado_produto_repositorio

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

app = FastAPI()
# pip install pymysql
# pip freeze > requirements.txt