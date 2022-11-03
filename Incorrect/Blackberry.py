class Blackberry:

    name = ""
    price = 0
    status = "Ok"

    def __init__(self, name, price, status):
        self.name = name
        self.price = price
        self.status = status

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name
        return True

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price
        return True

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status
        return True
