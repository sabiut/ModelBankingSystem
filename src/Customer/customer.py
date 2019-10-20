
class newCustomer:

    def __init__(self, account, name, address, phone, email, balance):
        self.account = account
        self.balance = balance
        self.name = name
        self.address = address
        self.phone = phone
        self.email = email

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email
    def getBalance(self):
        return self.balance

    def getAccount(self):
        return self.account


    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setPhone(self, phone):
        self.phone = phone

    def setEmail(self, email):
        self.email = email

    def setBalance(self, balance):
        self.balance = balance

    def setAccount(self, account):
        self.account = account



