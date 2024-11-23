class Almoxerifado:
    def _init_(self, nome):
        self.__nome = nome
        self.__itens = []

    def adicionar_item(self, item, usuario):
        if usuario.autenticacao:
            self.__itens.append(item)
        else:
            print("Usuario não autenticado. Por favor, faça o login para prosseguir")

    def remover_item(self, item, usuario):
        if usuario.autenticado == True:
            self.__itens.remove(item)
        else:
            print("Usuario não autenticado. Por favor, faça o login para prosseguir")

    def mostrar_todos_itens(self):
        for i in self.__itens:
            nome_temporario = i.passar_nome
            print(i.passar_nome)