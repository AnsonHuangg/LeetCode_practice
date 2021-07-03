class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        if carType==1 and self.big>0:
            self.big -= 1
            return bool(1)
        elif carType==2 and self.medium>0:
            self.medium -= 1
            return bool(1)
        elif carType==3 and self.small>0:
            self.small -= 1
            return bool(1)
        else:
            return bool(0)
