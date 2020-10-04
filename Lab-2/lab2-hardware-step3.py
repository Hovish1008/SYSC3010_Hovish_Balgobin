from sense_hat import SenseHat
import time

sense = SenseHat()

"""
    Part 3 of the lab understood from online codes and adapted to display live displays
    for temperature humidity and pressure.


"""

l=1

while l:
    sense.clear()
    temp=sense.get_temperature()
    pres=sense.get_pressure()
    hum=sense.get_humidity()
    #print (int(t)-23):
    for l in range (int(temp)-23):
        if l<8:
            sense.set_pixel(1,7-l,[255,0,0])
    for l in range (int(pres/2)-500):
        if l<8:
            sense.set_pixel(3,7-l,[0,255,0])

    for l in range (int(hum)-35):
        if l<8:
            sense.set_pixel(5,7-l,[0,0,255])

    time.sleep(10)
    
