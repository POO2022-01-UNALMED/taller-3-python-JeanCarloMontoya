class Control:
    def __init__(self):
        self._tv=0
    
    def enlazar(self,tv):
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
