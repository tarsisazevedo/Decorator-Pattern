#encoding: utf-8
from pyhistorian import *
from should_dsl import *

from cliente import *

from cafe_a_moda_da_casa import *
from decorators.decorator_whip import *
from decorators.decorator_leite import *

class PedindoUmCafeComAdicional(Historia):
    """
    Como um cliente da cafeteria
    Eu quero comprar um cafe com adicional
    Para que eu possa incrementar meu cafe
    """
    cenarios=['PedindoUmCafeAModaDaCasaComWhip', 'PedindoUmCafeAModaDaCasaComLeite']
    colored = True

class PedindoUmCafeAModaDaCasaComWhip(Cenario):
    @DadoQue("Eu sou um cliente")
    def eu_sou_um_cliente(self):
        self.cliente = Cliente()

    @DadoQue("e eu quero comprar um cafe a moda da casa")
    def cafe_a_moda_da_casa(self):
        self.cafe_a_moda_da_casa = CafeAModaDaCasa(0.99)

    @DadoQue("eu quero acrescentar whip no cafe")
    def cafe_com_whip(self):
        self.cafe_com_whip = Whip(self.cafe_a_moda_da_casa)

    @Quando("eu peço meu cafe, que custa 0.99, com whip, que custa 0.20")
    def pedir_cafe_com_whip(self):
        self.cliente.pedir_cafe(self.cafe_com_whip)

    @Entao("eu tenho meu cafe com whip e uma conta de 1.19")
    def eu_tenho_uma_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 1.19

class PedindoUmCafeAModaDaCasaComLeite(Cenario):
    DadoQue("Eu sou um cliente")
    DadoQue("e eu quero comprar um cafe a moda da casa")
    @DadoQue("eu quero acrescentar leite no meu cafe")
    def cafe_com_leite(self):
        self.cafe_com_leite = Leite(self.cafe_a_moda_da_casa)
    @Quando("eu peço meu cafe, que custa 0.99, com leite, que custa 0.50")
    def pedir_cafe_com_leite(self):
        self.cliente.pedir_cafe(self.cafe_com_leite)

    @Entao("eu tenho meu cafe com leite e uma conta de 1.49")
    def eu_tenho_uma_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 1.49

PedindoUmCafeComAdicional.run()
