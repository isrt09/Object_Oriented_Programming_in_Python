class Car:
    number_tires = 4

    def __init__(self):
        self.name    = "Toyota"
        self.brand   = "Corolla"
        self.country = "Japan"

    def start_engine(self):
        self.engine_running = True

    def stop_engine(self):
        self.stop_engine   = False

def main():
    new_car = Car()
    print("========= New Car Details ========== \n")
    print("New Car Name    : {}".format(new_car.name))
    print("New Car's Brand : {}".format(new_car.brand))
    print("Country of Car  : {}".format(new_car.country))

if __name__ == '__main__':
    main()