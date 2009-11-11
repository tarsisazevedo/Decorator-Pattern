from decorator_abstrato import *

class Leite(AbstractDecorator):
    def __init__(self, cafe):
        self.cafe = cafe

    def get_preco(self):
        return 0.50 + self.cafe.get_preco()
