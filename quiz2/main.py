class Main():
    def get(self):
        
        self.zumiez = Longboards()
        self.zumiez.trucks = "hard"
        self.zumiez.brand = "Zumiez"
        self.zumiez.velocity()
        print self.zumiez.speed
        
        self.penny = Pennyboards()
        self.penny.trucks = "hard"
        self.penny.brand = "Penny"
        self.penny.velocity()
        print self.penny.speed


class Longboards(object):
    def __init__(self):
        self.trucks = ""
        self.brand = ""
        self.distance = 100
        self.time = 60
        self.__speed = 0

        

    def velocity(self):
        s = self.distance/self.time
        self.speed = s


class Pennyboards(object):
    def __init__(self):
        self.trucks = ""
        self.wheels = ""
        self.brand = ""
        self.made_in = ""
        self.distance = 100
        self.time = 100
        self.speed = 0

        self.velocity()
        print self.__speed

    def velocity(self):
        s = self.distance/self.time
        self.speed = s

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, average_speed):
        self.__speed = average_speed