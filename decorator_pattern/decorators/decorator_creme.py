from decorator_abstrato import *

class Creme(AbstractDecorator):
    def __init__(self, cafe):
        self.cafe = cafe

    def get_preco(self):
        return 0.20 + self.cafe.get_preco()
