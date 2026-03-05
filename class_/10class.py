class Car:
    # Constructor (initializes the object)
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    # Method to accelerate the car
    def accelerate(self, increase):
        self.speed += increase
        print(f"The car accelerated. Current speed: {self.speed} km/h")

    # Method to brake the car
    def brake(self, decrease):
        self.speed