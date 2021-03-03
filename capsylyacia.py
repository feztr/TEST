class Point:
    def __init__(self, x=0,y=0):
        self.__x=x; self.__y=y
    def setCorrds(self,x,y):
        self.__x=x
        self.__y=y
    def getCoords(self):
        return self.__x, self.__y
pt=Point(1,2)
print(pt.getCoords())
pt.setCorrds(10,20)
print(pt.getCoords())