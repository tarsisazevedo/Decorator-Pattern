#encoding: utf-8
from pyhistorian import *
from should_dsl import *

from cliente import *

from cafe_a_moda_da_casa import *
from decorator_whip import *

class PedindoUmCafeComAdicional(Historia):
    """
    Como um cliente da cafeteria
    Eu quero comprar um cafe com adicional
    Para que eu possa incrementar meu cafe
    """

    colored = True

class PedindoUmCafeAModaDaCasaComWhip(Cenario):
    @DadoQue("Eu sou um cliente")
    def eu_sou_um_cliente(self):
        self.cliente = Cliente()

    @DadoQue("e eu quero compra um cafe a moda da casa com whip")
    def cafe_a_moda_da_casa_com_whip(self):
        self.cafe_a_moda_da_casa = CafeAModaDaCasa(0.99)
        self.cafe_com_whip = Whip(self.cafe_a_moda_da_casa)

    @Quando("eu peço meu cafe com whip")
    def pedir_cafe_com_whip(self):
        self.cliente.pedir_cafe(self.cafe_com_whip)

    @Entao("eu tenho meu cafe com whip e uma conta de 1.19")
    def eu_tenho_uma_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 1.19

PedindoUmCafeComAdicional.run()
