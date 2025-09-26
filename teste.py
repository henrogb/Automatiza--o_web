new_user = "teste da silva"

def login(nome_usuario):
    nome = new_user.split(" ")
    primeiro = nome[0]
    ultimo = nome[-1]
    log = f"{primeiro}.{ultimo}"
    return print(log)

login(new_user)