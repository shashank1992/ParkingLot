# ParkingLot
ParkingLot Assignment
From terminal can run using, python3 parking.py
In the interpreter, we can specify custom arguments as follows. 

import parking
parking.main(25,8,12)
parking.main accepts three arguments, number of cars , width and length of the parking slot respectively. 
eg. to attempt to park 10 cars with each spot of size 8ft*12ft , run parking.main(10,8,12)
We have assumed the default parking space as 2000ft2, can input the size as additional argument.
parking.main(25,8,12,size=4000)
