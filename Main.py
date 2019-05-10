from projectUI import Ui_projectWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import matplotlib.pyplot as plt
import time
import numpy as np
from datetime import datetime as dt

#pripojeni k DB
conn = sqlite3.connect('measurements.db')

#metoda pro ziskani minimalni a maximalni hodnotu pro teplotu
def getTempMinMax():
    minTmp = 0
    maxTmp = 0
    minDate = ""
    maxDate = ""

    #vyber dat z DB
    c = conn.cursor()
    for row in c.execute('SELECT date, max(data) FROM measurements WHERE type="teplota"'):
        maxDate = (row[0])
        maxTmp = (row[1])  
    for row in c.execute('SELECT date, min(data) FROM measurements WHERE type="teplota"'):
        minDate = (row[0])
        minTmp = (row[1])   

    #vlozeni hodnot do Labelu v GUI
    ui.tmpMaxLbl.setText("Max: "+str(maxTmp)+" °C, čas: " + maxDate)   
    ui.tmpMinLbl.setText("Min: "+str(minTmp)+" °C, čas: "+ minDate) 

#metoda pro ziskani minima a maxima pro vlhkost
def getHumMinMax():
    minHum = 0
    maxHum = 0
    minDate = ""
    maxDate = ""

    #vyber dat z DB
    c = conn.cursor()
    for row in c.execute('SELECT date, max(data) FROM measurements WHERE type="vlhkost"'):
        maxDate = (row[0])
        maxHum = (row[1])  
    for row in c.execute('SELECT max(data), date, min(data) FROM measurements WHERE type="vlhkost"'):
        minDate = (row[1])
        minHum = (row[2])   

    #vlozeni hodnot do Labelu v GUI
    ui.humMaxLbl.setText("Max: "+str(maxHum)+" %"+", čas: " + maxDate)   
    ui.humMinLbl.setText("Min: "+str(minHum)+" %"+", čas: "+ minDate) 

def getPrutokMinMax():
    minPrutok = 0
    maxPrutok = 0
    minDate = ""
    maxDate = ""

    c = conn.cursor()
    for row in c.execute('SELECT date, max(data) FROM measurements WHERE type="prutok"'):
        maxDate = (row[0])
        maxPrutok = (row[1])  
    for row in c.execute('SELECT max(data), date, min(data) FROM measurements WHERE type="prutok"'):
        minDate = (row[1])
        minPrutok = (row[2])   

    ui.prutokMaxLabel.setText("Max: "+str(maxPrutok)+" l/min, čas: " + maxDate)   
    ui.prutokMinLabel.setText("Min: "+str(minPrutok)+" l/min, čas: "+ minDate) 

def getTlakMinMax():
    minTlak = 0
    maxTlak = 0
    minDate = ""
    maxDate = ""

    c = conn.cursor()
    for row in c.execute('SELECT date, max(data) FROM measurements WHERE type="tlak"'):
        maxDate = (row[0])
        maxTlak = (row[1])  
    for row in c.execute('SELECT max(data), date, min(data) FROM measurements WHERE type="tlak"'):
        minDate = (row[1])
        minTlak = (row[2])   

    ui.tlakSpadMaxLabel.setText("Max: "+str(maxTlak)+" kPa, čas: " + maxDate)   
    ui.tlakSpadMinLabel.setText("Min: "+str(minTlak)+" kPa, čas: "+ minDate) 

#metoda pro vzkreslovani dat do grafu
def plotTmpData():
    #ziskani hodnot ze vstupniho casoveho pole odkdy dokdy se maji data vzkreslit
    fromV = ui.dateTimeEdit.dateTime()
    toV = ui.dateTimeEdit_2.dateTime()
    fromV = fromV.toPyDateTime().strftime("%Y-%m-%d %H:%M")
    toV = toV.toPyDateTime().strftime("%Y-%m-%d %H:%M")
  
    dates=[]
    values=[]
    c = conn.cursor()
    sql = ""
    if(ui.tmpRadioButton.isChecked()):
        plt.ylabel('teplota °C')
        sql = c.execute('SELECT date, data FROM measurements WHERE type="teplota" and date BETWEEN ? AND ? ',(fromV, toV))
    elif (ui.humRadioButton.isChecked()):
        plt.ylabel('vlhkost %')
        sql = c.execute('SELECT date, data FROM measurements WHERE type="vlhkost" and date BETWEEN ? AND ? ',(fromV, toV))
    elif (ui.prutokRadioButton.isChecked()):
        plt.ylabel('Průtok [l/min]')
        sql = c.execute('SELECT date, data FROM measurements WHERE type="prutok" and date BETWEEN ? AND ? ',(fromV, toV))
    elif (ui.spadRadioButton.isChecked()):
        plt.ylabel('tlak [kPa]')
        sql = c.execute('SELECT date, data FROM measurements WHERE type="tlak" and date BETWEEN ? AND ? ',(fromV, toV))

    for row in sql:
        dates.append(row[0][5:])
        values.append(row[1])  
    meanV = "0"
    maxV = "0"
    minV = "0"
    if(len(values) != 0):
        meanV = "Průměr: "+str(round((sum(values)/len(values)),2))
        maxV = "Max: "+str(max(values))
        minV = "Min: "+str(min(values))
    
    space = 0
    xticks = np.arange(len(values))
    #nastaveni casove osy X, aby se neukazovalo kazde datum
    if len(values) < 50:
        space = 2
    elif len(values) >= 50 and len(values)<100:
        space = 5
    else:
        space = 10

    #nastaveni grafu
    plt.plot(dates, values, '--bo')
    plt.title("Graf hodnot v závislosti na čase")
    ax = plt.gca()
    ax.set_ylim([min(values)-5,max(values)+10])
    plt.xlabel('čas')
    
    plt.grid()
    plt.tight_layout()
    plt.xticks(xticks[::space], dates[::space], rotation=45)
    plt.figtext(0.14,0.85, meanV, fontsize=9, bbox=dict(facecolor='wheat', alpha=1))
    plt.figtext(0.14,0.8, maxV, fontsize=9, bbox=dict(facecolor='wheat', alpha=1))
    plt.figtext(0.14,0.75, minV, fontsize=9, bbox=dict(facecolor='wheat', alpha=1))
    
    plt.show()

#metoda pro ziskani naposledky namerenych hodnot
def displayAll():
    c = conn.cursor()
    tempr=0
    hum=0

    sql = c.execute('SELECT data FROM measurements WHERE type="teplota" order by date desc limit 1')
    for row in sql:
        tempr = (row[0])
    
    sql = c.execute('SELECT data FROM measurements WHERE type="vlhkost" order by date desc limit 1')
    for row in sql:
        hum = (row[0])
    
    sql = c.execute('SELECT data FROM measurements WHERE type="tlak" order by date desc limit 1')
    for row in sql:
        tlak = (row[0])
    
    sql = c.execute('SELECT data FROM measurements WHERE type="prutok" order by date desc limit 1')
    for row in sql:
        prutok = (row[0])
    
    ui.tmpLabel.setText(str(tempr)+" °C")
    ui.humLabel.setText(str(hum) + " %")
    ui.prutokLabel.setText(str(prutok)+ " l/min")
    ui.spadLabel.setText(str(tlak) + " kPa")
    getTempMinMax()
    getHumMinMax()
    getPrutokMinMax()
    getTlakMinMax()

#Main, pouziti UI a metod pri stisknu tlacitek
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    projectWindow = QtWidgets.QMainWindow()
    ui = Ui_projectWindow()
    ui.setupUi(projectWindow)
    ui.measureAllBtn.clicked.connect(displayAll)
    ui.datePlotButton.clicked.connect(plotTmpData)
    
    projectWindow.show()
    sys.exit(app.exec_())