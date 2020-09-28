import sys                  #Importing sys library for interacting with interpreter
import RPi.GPIO as GPIO     #Importing Raspberry Pi library
from time import sleep      #Adds delay to your program
import Adafruit_DHT         #Importing Adafruit DHT sensor library
import urllib2,json         #Importing URL library to read write data on websites

WRITE_API_KEY='9T20YLZP0HY478WQ'#Write your Thingspeak Write API Key

GPIO.setmode(GPIO.BCM)      #setting up Raspberry to GPIO chip mode
GPIO.setwarnings(False)     #removes unwanted warnings
GPIO.setup(18,GPIO.OUT)     #defining GPIO pin number 18 as Output
GPIO.setup(17,GPIO.OUT)     #defining GPIO pin number 17 as Output


def getSensorData():        #Function to read DHT11 sensor data

    Humid, Temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)   #Reading Temperature and Humidity value from GPIO pin 23
    return (str(Humid), str(Temp))  #Return string Humidity and Temperature data


#main() function definition
def main():
        #Writing data to Thingspeak Server
    print ('starting...')
    baseURL = 'https://api.thingspeak.com/update?api_key=%s'%(WRITE_API_KEY) #Starting the connection to Thingspeak Server
    while True:     #Condition for repetitive running of the loop
        try:
            RH,T = getSensorData()
            #Read the value of sensor data from the getSensorData function and store it in RH and
            #T variables
            req = urllib2.Request(url=baseURL+'&field2=%s&field1=%s'%(RH,T))
            #Updating the Humidity and Temperature data on thingspeak



            #Reading the sensor data from Thingspeak website
            connect1 = urllib2.urlopen(req) #Requesting the Thingspeak server for communicating
            print connect1.read()           #Print the values which we read from thingspeak
            print("Humidity" +str(RH)+ "%")    #Printing the Humidity values
            print("Temperature" +str(T)+ "C")  #Printing the Humidity values
            connect1.close()                #Closing the connection with Thingspeak

            connect2 = urllib2.urlopen('https://matroclinous-intell.000webhostapp.com/buttonStatus.php')
            #Requesting your website for establishing connection
            response = connect2.read()  #Reading the input from the website and saving it to response variable
            print response              #Print the response which we get from the website


            #Condition for turning ON and turning OFF of the relay driver
            if response == 'ON':
                print "fan on"
                GPIO.output(18,GPIO.LOW)
                #Relaystate=true

            elif response == 'OFF':
                print "fan off"
                GPIO.output(18,GPIO.HIGH)
                #Relaystate=false

            elif response == 'ON1':
                print "light on"
                GPIO.output(17,GPIO.LOW)
                #Relaystate=true

            elif response == 'OFF1':
                print "light off"
                GPIO.output(17,GPIO.HIGH)
                #Relaystate=false

            connect2.close()        #Closing the connection with website
            sleep(3)                #Delay of 3 seconds
        except:             #Exception Block for handling exceptions
            print 'Exiting.'
            break


# calling main program
if __name__ == '__main__':
    main()
