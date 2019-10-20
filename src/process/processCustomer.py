from src.Customer.customer import newCustomer

class processCustomer(newCustomer):

    def display(self):
        print("Account Number:", self.account, "\nCustomer name:", self.name, "\n" "Address:", self.address,
              "\nPhone:", self.phone, "\nEmail:", self.email, "\nBalance:", "$",self.balance)


    def deposit(self,deposit):
        self.balance += deposit
        print("you have deposit", "$",format(deposit), "into account:", self.account,
              "\nYour new balance is", "$",self.balance)

    def withdraw(self,withdraw):
        if self.balance-withdraw < 0:
            print(" You have insufficient fund in your account")
        else:
            self.balance -=withdraw
            print("You have withdwar","$",withdraw, " your new balance is","$", self.balance)
