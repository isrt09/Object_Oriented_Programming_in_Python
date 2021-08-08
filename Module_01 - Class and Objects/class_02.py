class Car:
    number_tires = 4

    def __init__(self,name, brand,country):
        self.name    = name
        self.brand   = brand
        self.country = country

    def start_engine(self):
        self.engine_running = True

    def stop_engine(self):
        self.stop_engine   = False

def main():
    print("========= Toyota Car Details ==========")
    _toyota = Car("Toyota","Toyota_M2312","Japan")
    print("New Car Name    : {}".format(_toyota.name))
    print("New Car's Brand : {}".format(_toyota.brand))
    print("Country of Car  : {}\n".format(_toyota.country))

    print("========= Ford Car Details ==========")
    _ford = Car("The Ford", "Ford_F1281", "Germany")
    print("New Car Name    : {}".format(_ford.name))
    print("New Car's Brand : {}".format(_ford.brand))
    print("Country of Car  : {}\n".format(_ford.country))

    print("========= Ferreri Car Details ==========")
    _ferreri = Car("The Ferreri", "Ferreri_F0021", "USA")
    print("New Car Name    : {}".format(_ferreri.name))
    print("New Car's Brand : {}".format(_ferreri.brand))
    print("Country of Car  : {}\n".format(_ferreri.country))

if __name__ == '__main__':
    main()