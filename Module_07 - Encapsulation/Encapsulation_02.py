# Simple Encapsulation Mechanism in Python
class Father:
    def __init__(self,account):
        self.account = account
        self._account = account
        self.__account = account

obj = Father('FDR')
print('Public Account is ready',obj.account)
print('Protected Account is ready',obj._account)
print('Private Account is ready',obj._Father__account)
