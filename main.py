class ControleEstoque:
    def __init__(self):
        self.estoque = {}

    def adicionar_item(self, item, quantidade):
        if item in self.estoque:
            self.estoque[item] += quantidade
        else:
            self.estoque[item] = quantidade

    def remover_item(self, item, quantidade):
        if item in self.estoque:
            if quantidade >= self.estoque[item]:
                del self.estoque[item]
            else:
                self.estoque[item] -= quantidade

    def verificar_estoque(self, item):
        if item in self.estoque:
            return self.estoque[item]
        else:
            return 0

    def listar_itens(self):
        return self.estoque.keys()


def main():
    controle = ControleEstoque()

    # Adiciona alguns itens ao estoque inicial
    controle.adicionar_item("Maçã", 100)
    controle.adicionar_item("Banana", 150)
    controle.adicionar_item("Laranja", 200)

    # Remove alguns itens do estoque inicial
    controle.remover_item("Maçã", 30)
    controle.remover_item("Banana", 50)

    # Exibe o estoque atual de alguns itens
    print("Estoque de Maçã:", controle.verificar_estoque("Maçã"))
    print("Estoque de Banana:", controle.verificar_estoque("Banana"))
    print("Estoque de Laranja:", controle.verificar_estoque("Laranja"))

    # Lista todos os itens disponíveis no estoque
    print("Itens disponíveis no estoque:", controle.listar_itens())


if __name__ == "__main__":
    main()
