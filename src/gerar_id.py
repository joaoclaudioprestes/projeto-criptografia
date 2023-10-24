import uuid

def gerar_id():
    return str(uuid.uuid4())[:4]