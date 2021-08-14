class Bank:

    name = "Sonali Bank"

    @staticmethod
    def deposit(amount):
        return amount

    @staticmethod
    def account_number(number):
        return number

    @classmethod
    def branch_name(cls):
         return cls.name

account        = Bank()
deposit_amount = account.deposit(30000)
account_number = account.account_number(10000164786)
branch_name    = Bank.branch_name()

print("Bank Deposit is {} Taka Only".format(deposit_amount))
print("Bank Account Number is AC-{} ".format(account_number))
print("Bank Account Branch is {}".format(branch_name))