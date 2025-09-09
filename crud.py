from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/") 
db = client["meu_banco"]  
colecao = db["usuarios"]   


def criar_usuario(nome, idade):
    usuario = {"nome": nome, "idade": idade}
    colecao.insert_one(usuario)
    print(f"Usuário {nome} criado!")


def listar_usuarios():
    for usuario in colecao.find():
        print(usuario)


def atualizar_usuario(nome, novo_nome=None, nova_idade=None):
    filtro = {"nome": nome}
    atualizacao = {}
    if novo_nome:
        atualizacao["nome"] = novo_nome
    if nova_idade:
        atualizacao["idade"] = nova_idade
    if atualizacao:
        colecao.update_one(filtro, {"$set": atualizacao})
        print(f"Usuário {nome} atualizado!")
    else:
        print("Nada para atualizar.")

def deletar_usuario(nome):
    resultado = colecao.delete_one({"nome": nome})
    if resultado.deleted_count:
        print(f"Usuário {nome} deletado!")
    else:
        print(f"Usuário {nome} não encontrado.")


if __name__ == "__main__":
    criar_usuario("Matheus", 25)
    criar_usuario("Ana", 30)
    print("\nLista de usuários:")
    listar_usuarios()
    
    atualizar_usuario("Matheus", nova_idade=26)
    print("\nLista de usuários após atualização:")
    listar_usuarios()
    
    deletar_usuario("Ana")
    print("\nLista de usuários após exclusão:")
    listar_usuarios()
