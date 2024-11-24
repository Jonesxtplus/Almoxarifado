class Usuario:
    def __init__(self, nome, senha, autenticado):
        self.__nome = nome
        self.__senha = senha
        self.__autenticado = False
    
    def login(self):
        senha = input("Digite sua senha: ")
        if senha == self.__senha:
            self.__autenticado = True
            print(f"O usuário {self.__nome} foi logado")
            return self.__autenticado
        else:
            print("Senha incorreta. Digite uma senha válida!")
            return self.__autenticado
    
    def modificar_senha(self, nome):
        senha_atual = input("Digite sua senha atual: ")
        if senha_atual == self.__senha:
            nova_senha = input("Digite a nova senha: ")
            confirma_senha = input("Confirme a senha: ")
            if confirma_senha == nova_senha:
                self.__senha = nova_senha
                print("Senha alterada com sucesso!")
            else:
                print("As senhas digitadas não são iguais, tente novamente.")
        else:
            print("A senha está incorreta!")