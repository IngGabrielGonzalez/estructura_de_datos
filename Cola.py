class Cola:
    def __init__(self):
        self.lista = []

    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        for item in self.lista:
            yield item

    def __str__(self):
        return str(self.lista)
    
    def agregarCola(self,item):
        self.lista.append(item)

    def extrarDeLaCola(self):
        return self.lista.pop(0)
    
    def limpiar(self):
        self.lista0=[]

