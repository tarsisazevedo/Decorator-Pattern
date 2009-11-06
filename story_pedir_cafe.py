#encoding: utf-8

from pyhistorian import *
from should_dsl import *

from cafe_a_moda_da_casa import *
from cafe_espresso import *
from cafe_descafeinado import *
from cafe_preto import *

from cliente import *

class PedindoUmCafeSimples(Historia):
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

    @Entao("eu tenho meu café e uma conta de 0.99")
    def eu_tenho_uma_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 0.99

class PedindoUmCafeEspresso(Cenario):
    @DadoQue("eu sou um cliente e quero tomar um cafe espresso")
    def criar_cafe_espresso(self):
        self.cliente = Cliente()
        self.cafe_espresso = CafeEspresso(1.10)

    @Quando("Eu peço um cafe espresso")
    def pedir_cafe_espresso(self):
        self.cliente.pedir_cafe(self.cafe_espresso)

    @Entao("eu tenho meu cafe e uma conta de 1.10")
    def eu_tenho_uma_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 1.10

class PedindoUmCafeDescafeinado(Cenario):
    @DadoQue("Eu sou um cliente e quero tomar um cafe descafeinado")
    def criar_cafe_descafeinado(self):
        self.cliente = Cliente()
        self.cafe_descafeinado = CafeDescafeinado(0.70)

    @Quando("eu peço um cafe descafeinado")
    def pedir_cafe_descafeinado(self):
        self.cliente.pedir_cafe(self.cafe_descafeinado)

    @Entao("eu tenho meu cafe e uma conta de 0.70")
    def eu_tenho_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 0.70

class PedindoUmCafePreto(Cenario):
    @DadoQue("eu sou um cliente e quero tomar um cafe preto")
    def criar_cafe_preto(self):
        self.cliente = Cliente()
        self.cafe_preto = CafePreto(0.50)

    @Quando("eu peço um cafe preto")
    def pedir_cafe_preto(self):
        self.cliente.pedir_cafe(self.cafe_preto)

    @Entao("eu tenho meu cafe e uma conta de 0.50")
    def eu_tenho_uma_conta(self):
        self.cliente.get_conta() |should_be.equal_to| 0.50

PedindoUmCafeSimples.run()
