
def deco_m_i(m):
    def m_interno(self):
        print("servimos la comida")
        m(self)
        print("termino de comer")
    return m_interno

class animal:
    def __init__(self,comida):
        self.comida = comida
    @deco_m_i
    def comer(self):
        print("el animal comio",self.comida)

fido = animal("croquetas")
fido.comer()
