class Customer:

    def __init__(self,name,address,phone,email):
        self.name=name
        self.address=address
        self.phone=phone
        self.email=email

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email


    def setName(self,name):
        self.name = name

    def setAddress(self,address):
        self.address=address
