class Control:
    def __init__(self):
        self._tv=0
    
    def enlazar(self,tv):
        if type(tv)==TV:
            self._tv=tv
            self._tv.control=self

    def turnOn(self):
        self._tv.turnOn()
    def turnDown(self):
        self._tv.turnDown()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()    
    def volumenUp(self):
        self._tv.volumenUp() 
    def volumenDown(self):
        self._tv.volumenDown()
    def setCanal(self,canal):
        self._tv.setCanal(canal)

    def setTv(self,tv):
        if type(tv)==TV:
            self._tv=tv
    def getTv(self):
        return self._tv


class Marca:
    def __init__(self,nombre):
        self._nombre=nombre
    def getNombre(self):
        return self._nombre
    def setNombre(self,nombre):
        self._nombre=nombre

class TV:
    numTV=0
    def __init__(self,marca,estado):
        self._marca=marca
        self._estado=estado
        self._canal=1
        self._precio=500
        self._volumen=1
        self.control=0
        TV.numTV+=1
    def getEstado(self):
        return self._estado

    def turnOn(self):
        self._estado=True
    def turnOff(self):
        self._estado=False

    def setMarca(self,marca):
        self._marca=marca
    def getMarca(self):
        return self._marca

    def setControl(self,control):
        self.control=control
    def getControl(self):
        return self.control
    
    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self,volumen):
        if self._estado==True:
            if volumen>=1 and volumen<=7:
                self._volumen=volumen
    def getVolumen(self):
        return self._volumen
    
    def setCanal(self,canal):
        if self._estado==True:
            if canal>=120 and canal<=1:
                self._canal=canal
    def getCanal(self):
        return self._canal
    
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    @classmethod
    def setNumTV(cls,numero):
        cls.numTV=numero

    def volumenUp(self):
        if self._estado==True:
            if self._volumen<7:
                self._volumen+=1
    def volumenDown(self):
        if self._estado==True:
            if self._volumen>1:
                self._volumen-=1
    def canalUp(self):
        if self._estado==True:
            if self._canal<120:
                self._canal+=1
    def canalDown(self):
        if self._estado==True:
            if self._canal>1:
                self._canal-=1

    
    









