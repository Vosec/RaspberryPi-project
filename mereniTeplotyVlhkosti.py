import sys
import Adafruit_DHT
import sqlite3
from datetime import datetime
from time import sleep
while True:
    conn = sqlite3.connect('measurements.db')
    #cteni z GPIO 4, DHT11 senzor
    humidity, temperature = Adafruit_DHT.read_retry(11, 4)
    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #kdyz cidlo funguje (nekdy hazelo nesmyslne hodnoty), ulozit do DB
    if(humidity<90):
        c = conn.cursor()
        c.execute("INSERT INTO measurements VALUES (?, ?, ?)", (date, "teplota", temperature))
        c.execute("INSERT INTO measurements VALUES (?, ?, ?)", (date, "vlhkost", humidity))
        conn.commit()
    print(date)
    print(temperature)
    print(humidity)
    sleep(15)
