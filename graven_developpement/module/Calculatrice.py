class Calculatrice:
    def __init__(self,a,b):
        self.entierA = a;
        self.entierB = b;

    def addition(self):
        return  self.entierA + self.entierB

    def multiplication(self):
        return self.entierB * self.entierA

def quickAdd(a,b):
    return a+b