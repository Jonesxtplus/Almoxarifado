class Item:
    def _init_(self, nome, quantidade, valor):
        self.__nome = nome
        self.__quantidade = quantidade
        self.__valor = valor

    @property
    def passar_nome(self):
        return self.__nome
    
    def mostrar_informacoes(self):
        print(self.__nome)
        print(self.__quantidade)
        print(self.__valor)

    def quantificar(self, valor):
        if valor < 0:
            raise ValueError("O valor do item não pode ser negativo")
        self.__valor = valor
        return self.__valor