class Stack:
    def __init__(self):
        self.lista = [];

    def __len__(self):
        return len(self.lista);


    def __iter__(self):
        for item in self.lista:
            yield item

    def __str__(self):
        return str(self.lista)
    
    def apilar(self, item):
        self.lista.append(item)

    def desapilar(self):
        return self.lista.pop()
    
    def limpiarSalida(self):
        self.lista=[]