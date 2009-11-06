from bebida import Bebida

class CafeEspresso(Bebida):
    def __init__(self, preco):
        self.preco = preco

    def get_preco(self):
        return self.preco
