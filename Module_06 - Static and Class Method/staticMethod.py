class Math:
    @staticmethod
    def add(number):
        return number + 100

    @staticmethod
    def division(number):
        return number / 2

    @staticmethod
    def inifity():
        print("Invalid Number")

print(Math.add(100))
print(Math.division(100))
print(Math.inifity())