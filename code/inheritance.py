#Inheritance

class Fruit:
    color=""

    def __init__(self,color,size):
        self.color=""
        self.size=""


class Apple(Fruit):
    size=""

    def printFruitDetails(self):
        print("Apple is of {} color & is a {} size fruit.".format(self.color,self.size))


a=Apple('red','medium')
a.printFruitDetails()
