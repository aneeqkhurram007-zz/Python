from math import pi


class cylinder():

    def __init__(self, * args):
        self.setRadius(args[0])
        self.setHeight(args[1])

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setHeight(self, height):
        self.__height = height

    def getHeight(self):
        return self.__height

    def computeArea(self):
        return (2*pi*self.getRadius()*self.getRadius())+self.getHeight()*(2*pi*self.getRadius())

    def computeVolume(self):
        return (pi*self.getRadius()*self.getRadius()*self.getHeight())

    def __str__(self):
        return "Area of sylinder = "+str(self.getRadius())+" and height = "+str(self.getHeight())+" : "+str(self.computeArea())+"\n Volume of sylinder = "+str(self.computeVolume())

    def setCylinderData(self, *args):
        self.setRadius(args[0])
        self.setHeight(args[1])
