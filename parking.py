from random import choice
from random import randint
import json

class ParkingLot:
    def __init__(self,size=2000,w=8,l=12):
        self.capacity = size//(w*l)
        self.arr = [0]*self.capacity
    
    def get_json(self):
        d = {}
        for i,car in enumerate(self.arr):
            d[car] = i
        with open('parking.json','w') as outfile:
            json.dump(d,outfile)  

class Car:
    def __init__(self,license):
        self.license = license
    
    def __str__(self) -> str:
        return str(self.license)

    def park(self,parking_lot,spot):
        if spot > len(parking_lot.arr) or not parking_lot.arr[spot] == 0:
            return 400
        else :
            parking_lot.arr[spot] = self.license
            parking_lot.capacity -=1
            return 200


def fill(cars, parking_lot,w=8,l=12):
    i =0
    car_objs = []
    for car in cars:
        car_objs.append(Car(car))
    sequence = [i for i in range(parking_lot.capacity)]
    while i < len(car_objs) and parking_lot.capacity > 0:
        spot = choice(sequence)
        status = car_objs[i].park(parking_lot,spot)
        if status ==200:
            print("car with license plate %s parked successfully in spot %d" %(car_objs[i],spot))
            i+=1
        else:
            print("car with license plate %s attempted to park in spot %d, but failed" %(car_objs[i],spot))
    print('Successfully parked %d cars' %i)

def main(capacity = 25,w=8,l=12,**kwargs):
    cars = [randint(999999,10000000) for _ in range(capacity)]
    if kwargs.get('size',None):
        size = kwargs.get('size')
    else: size = 2000
    parking_lot = ParkingLot(size,w,l)
    fill(cars,parking_lot,w,l)
    parking_lot.get_json()

if __name__=='__main__':
    main()