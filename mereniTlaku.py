
#i2cdetect -y 1    prikaz pro zjisteni I2C 
from smbus import SMBus
from time import sleep
import sqlite3
from datetime import datetime

conn = sqlite3.connect('measurements.db')
bus = SMBus(1)
print("Read the A/D")
print("Ctrl C to stop")

#zaslani konfiguracniho bytu
reg = int('10010000',2)
bus.write_byte(0x6c, reg)

#pocitadlo poctu mereni pro prumer 10ti hodnot
count = 0
p = []
while(True):
   print('-------')
   count += 1
   #cteni bytu, prevod do binaru, odriznuti nepotrebnych bitu, znovu do 10tkove soustavy, prepocet pro napeti a pro tlak
   block = bus.read_i2c_block_data(0x6c, 0, 3)
   s1 = '{:08b}'.format(block[0])
   s2 = '{:08b}'.format(block[1])
   print(s1)
   print(s2)
   s1 = s1[4:]
   res = ''.join([s1,s2])
   print(res)
   res = int(res,2)
   print(res)
   
   volts = (4.096/4096)*res
   print(volts)
   print(block)
   
   p.append((100 * volts) - 1)
   
   #pro 10 namerenych hodnot udelat prumer a ulozit do DB
   if count == 10:
       val = 0
       prum = 0
       for i in p:
           val += i
       prum = val/len(p)
       print("prumer tlaku: ", end=' ')
       print(prum)
       date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       c = conn.cursor()
       c.execute("INSERT INTO measurements VALUES (?, ?, ?)", (date, "tlak", prum))
       conn.commit()
       p = []
       count = 0
   
   #merit kazdych 5 vterin
   sleep(5)
   

