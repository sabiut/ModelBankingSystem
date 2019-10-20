from src.process.processCustomer import processCustomer

def start():
    firstcustomer=processCustomer("ABI847362", "James Ben", "Tralee Place", "2658723", "jben@gmail.com", 6000)
    secondcustomer = processCustomer("AAI847362", "Kenson Thomas", "Siladel", "2636547", "kt@gmail.com", 10000)
    firstcustomer.display()
    # uncomment the line below to test
    #firstcustomer.deposit(8976)
    #firstcustomer.withdraw(900)



if __name__=="__main__":
    start()