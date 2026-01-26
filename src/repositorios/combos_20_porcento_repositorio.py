from sqlalchemy.orm import Session, contains_eager

from src.database.models import Combo_20_Porcento


def obter_todos(db: Session):
    combos = db.query(Combo_20_Porcento).options(contains_eager(Combo_20_Porcento.teclado)).options(contains_eager(Combo_20_Porcento.mouse)).all()

    combos_20 = []
    for combo in combos:
        preco_total = combo.mouse.preco + combo.teclado.preco

        valor_desconto =  preco_total / 5

        preco_final = preco_total - valor_desconto

        combo = {
            "id" : combo.id,
            "nome_promocao" : combo.nome_combo,
            "mouse" : combo.mouse,
            "teclado" : combo.teclado,
            "preco_total": preco_total,
            "porcentagem_desconto": "20%",
            "valor_desconto": valor_desconto,
            "preco_final": preco_final
        }

        combos_20.append(combo)

    return combos_20


def cadastrar_combo(db: Session, nome_combo : str, id_mouse : int, id_teclado : int):
    combo = Combo_20_Porcento(nome_combo= nome_combo, id_mouse=id_mouse, id_teclado=id_teclado)

    db.add(combo)
    db.commit()
    db.refresh(combo)
    return combo


def editar_combo(db: Session, id: int, nome_combo : str, id_mouse : int, id_teclado : int):
    combo = db.query(Combo_20_Porcento).filter(Combo_20_Porcento.id == id).first()

    if not combo: 
        return 0

    combo.nome_combo = nome_combo
    combo.id_mouse = id_mouse
    combo.id_teclado = id_teclado

    db.commit()
    return 1


def apagar_combo(db: Session, id: int):
    combo_para_apagar = db.query(Combo_20_Porcento).filter(Combo_20_Porcento.id == id).first()

    if not combo_para_apagar:
        return 0
    
    db.delete(combo_para_apagar)
    db.commit()

    return 1


def obter_combo_por_id(db: Session, id: int):
    combo = db.query(Combo_20_Porcento).filter(Combo_20_Porcento.id ==id).options(contains_eager(Combo_20_Porcento.mouse)).options(contains_eager(Combo_20_Porcento.teclado)).first()

    if not combo:
        return 0
    
    preco_total = combo.mouse.preco + combo.teclado.preco

    valor_desconto =  preco_total / 5

    preco_final = preco_total - valor_desconto
    return {
            "id" : combo.id,
            "nome_promocao" : combo.nome_combo,
            "mouse" : combo.mouse,
            "teclado" : combo.teclado,
            "preco_total": preco_total,
            "porcentagem_desconto": "20%",
            "valor_desconto": valor_desconto,
            "preco_final": preco_final
        }
