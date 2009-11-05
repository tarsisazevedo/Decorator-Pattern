#encoding: utf-8

from pyhistorian import *
from should_dsl import *

from cafe_a_moda_da_casa import *
from cliente import *

class PedindoUmCafe(Historia):
    """
    Como um cliente da cafeteria
    Eu quero pedir um tipo de café 
    Para que eu possa toma-lo
    """
    
    colored = True

class PedindoUmCafeAModaDaCasa(Cenario):
    @DadoQue("Eu sou um cliente e quero tomar um cafe a moda da casa")
    def criar_cafe_a_moda_da_casa(self):
        self.cliente = Cliente()
        self.cafe_a_moda_da_casa = CafeAModaDaCasa(0.99)

    @Quando("Eu peço o cafe a moda da casa")        
    def pedir_cafe_a_moda_da_casa(self):
        self.cliente.pedir_cafe(self.cafe_a_moda_da_casa)

    @Entao("eu tenho meu café e uma divida de 0.99")
    def eu_tenho_uma_divida(self):
        self.cliente.get_conta() |should_be.equal_to| 0.99

PedindoUmCafe.run()
