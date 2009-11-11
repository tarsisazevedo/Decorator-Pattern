from bebida import *

class Cliente:
    def pedir_cafe(self, cafe):
        self.cafe = cafe
        self.conta = self.cafe.get_preco()

    def get_conta(self):
        return self.conta
