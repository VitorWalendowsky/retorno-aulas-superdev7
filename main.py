from fastapi import Depends, FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

app = FastAPI()


# Teste

# 4 crus (2 por aluno)

#PeriPecas:
# - Monitor (Tamanho x"- Frequencia Hz - Preco R$ - Loja)

# - Notebook (Tamanho Tela" - Memoria RAM GB - Preco R$ - Loja - placa de video - marca da placa de video - RGB S/N - peso kg - SSD S/N)

# - Teclado (Preco R$ - modelo - Conexão - Cor)

# - Mouse (Preco R$ - modelo - DPI - Gamer ou Não(RGB) - Quantidade de botão)

# pip install pymysql
# pip freeze > requirements.txt