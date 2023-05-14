class Figura2D:
    pass

class Circulo(Figura2D):
    def __init__(self,radio):
        self.radio = radio
        self.pi = 3.1416


    def area(self):
        return self.pi*(self.radio**2)

    def perimetro(self):
        return (self.pi*2)*self.radio



class Cuadrado(Figura2D):
    def __init__(self,lado):
        self.lado = lado


    def area(self):
        return self.lado**2

    def perimetro(self):
        return self.lado*4


class Prisma:
    def __init__(self,base,altura):
        if isinstance(base,Figura2D) == True and isinstance(altura,float):
            self.base = base
            self.altura =altura
        else:
            raise TypeError("unsupported argument type(s)")
        

    def volumen(self):
        areaBase = self.base.area()

        return areaBase * self.altura
    
    def superficie(self):
        areaBase = self.base.area()
        perimetroBase = self.base.perimetro()
        areaPerimetro = areaBase + areaBase + perimetroBase
        return areaPerimetro * self.altura


class Cilindro(Prisma):
    def __init__(self,figura,altura):
        super().__init__(figura,altura)
        self.radio = self.base.radio


    def getRadio(self):
        return self.radio
    
    def getAltura(self):
        return self.altura

circulo = Circulo(5)
cuadrado = Cuadrado(4)

prisma = Prisma(circulo,2.4)

cilindro = Cilindro(circulo,2.4)


print(cilindro.getRadio())
