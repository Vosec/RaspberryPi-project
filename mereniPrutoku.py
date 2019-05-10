import RPi.GPIO as GPIO
from time import sleep
import sqlite3
from datetime import datetime
import time

i=0
#pro pouzivani cisel jako pinu GPIO 17, 2 atd..
GPIO.setmode(GPIO.BCM)
start = 0
#GPIO pin 17
Input_Sig = 17
GPIO.setup(Input_Sig, GPIO.IN)

#prisla vzestupna hrana
def interrupt_service_routine(Input_Sig):
    global i
    sleep(0.005) # edge debounce of 5mSec
    
    #pokud to je opravda vzestupna hrana tzv. opravdu protekly litr
    if GPIO.input(Input_Sig) == 1:
        #litr za minutu, doplnovat stary hodnoty
        if(i==0):
            global start
            start = datetime.now()
            i+=1
        if(i>=1):
            now = datetime.now()
            duration = now - start
            print(start)
            print(i)
            #pokud ubehla minuta, ulozit do DB
            if(duration.total_seconds() >= 60):
                print("minuta")
                #pocet litru za minutu
                conn = sqlite3.connect('measurements.db')
                c = conn.cursor()
                date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                c.execute("INSERT INTO measurements VALUES (?, ?, ?)", (date, "prutok", i-1))
                conn.commit()
                print("litru za minutu: ", end = ' ')
                print(i-1)
                i = 0
            else:
                i+=1
        
        print("RISING")
    return

GPIO.add_event_detect(Input_Sig, GPIO.RISING, callback=interrupt_service_routine, bouncetime=5)

try:
        while True:
            pass
            
except KeyboardInterrupt:
        pass
finally:
        print("\nRelease the used pin(s)")
        GPIO.cleanup([Input_Sig])