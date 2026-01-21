from fastapi import Depends, FastAPI, HTTPException

from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.orm import Session

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