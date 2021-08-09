class Factory:
    def __init__(self, make, brand, model, color, country):
        self.make    = make
        self.brand   = brand
        self.model   = model
        self.color   = color
        self.country = country

    # Destructor    
    def __del__(self):
        print("Destructor Involked...".format(self.make,self.brand))

def manufacture():
    toyota = Factory("Car","Toyota", "TYM2310","White","Japan")
    print("================== Manufacture Car Details ===============")
    print("Type  : {}".format(toyota.make))
    print("Brand : {}".format(toyota.brand))
    print("Model : {}".format(toyota.model))
    print("Color : {}".format(toyota.color))
    print("Country : {}\n".format(toyota.country))

    ferreri = Factory("Sports", "Ferreri", "FER2310", "Red", "Germany")
    print("================== Manufacture Car Details ===============")
    print("Type  : {}".format(ferreri.make))
    print("Brand : {}".format(ferreri.brand))
    print("Model : {}".format(ferreri.model))
    print("Color : {}".format(ferreri.color))
    print("Country : {}\n".format(ferreri.country))

    bmw = Factory("Executive", "BMW", "BM7310", "Black", "USA")
    print("================== Manufacture Car Details ===============")
    print("Type  : {}".format(bmw.make))
    print("Brand : {}".format(bmw.brand))
    print("Model : {}".format(bmw.model))
    print("Color : {}".format(bmw.color))
    print("Country : {}\n".format(bmw.country))

    print("================== Manufacture Car Delete ===============")
    # Destructor
    del bmw
    del toyota

if __name__ == '__main__':
    manufacture()


































