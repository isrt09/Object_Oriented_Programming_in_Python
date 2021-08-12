class Account:

    def deposit(self):
        print("20,000 Taka Only")

    def withdraww(self):
        print("50,000 Taka Only")

class Customer(Account):
    def __init__(self, username, email, password):
        self.username = username
        self.email    = email
        self.password = password

    def update_info(self,_username):
        self.username = _username

    def __str__(self):
        return self.username + " " + self.email + " " + self.password

    def __eq__(self, other):
        if self.username == other.username:
            print("Yes, Valid user")
        else:
            print("Sorry, Invalid User..Please Sign Up..")
        return False

    __repr__ = __str__

c1 = Customer('userPHP','userPHPgmail.com', 'adminPHP1234')
c2 = Customer('userJava','userJava@gmail.com', 'adminJava2345')
c3 = Customer('userPython','userPython@gmail.com', 'adminPython2345')

customers = [c1, c2, c3]

for customer in customers:
    print(customer)

print("".center(50,"="))

print("Customer 1 : ", c1)
c1.update_info("userMobileApplication")
print("Customer 1 :  {} (Updated)".format(c1))
print("Customer 2 : ", c2)
print("Customer 3 : ", c3)

print("".center(50,"="))

print("Customer 1 will be deposit the Bank for at least ",c1.deposit())
print("Customer 1 will be withdrawn the Bank for at least ",c1.withdraww())