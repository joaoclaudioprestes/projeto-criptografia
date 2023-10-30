import uuid  # Importa o módulo uuid para geração de identificadores únicos

def gerar_id():
    return str(uuid.uuid4())[:4]  # Retorna os primeiros 4 caracteres de um UUID v4
