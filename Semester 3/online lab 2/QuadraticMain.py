from math import sqrt


class Quadratic:
    def __init__(self, a, b, c):
        self.a = a
        self.b = a
        self.b = a

    def discCalc(self):

        self.disc = (self.b*self.b)-(4*self.a*self.b)
        return self.disc

    def computeRoots(self):
        if self.discCalc() >= 0:
            self.X1 = (-self.b-sqrt(self.discCalc()))/(2*self.a)
            self.X2 = (-self.b+sqrt(self.discCalc()))/(2*self.a)
        else:
            self.disc = -self.disc
            self.X1 = (-self.b-sqrt(self.disc))/(2*self.a)
            self.X2 = (-self.b+sqrt(self.disc))/(2*self.a)

    def display(self):
        self.computeRoots()
        if self.discCalc() >= 0:
            print("X1 = "+str(self.X1)+" X2 = "+str(self.X2))
        else:
            print("X1 = "+str(self.X1)+"i , X2 = "+str(self.X2)+"i")


a = float(input("Enter value for A: "))
b = float(input("Enter value for B: "))
c = float(input("Enter value for C: "))

qroots = Quadratic(a, b, c)
qroots.display()
