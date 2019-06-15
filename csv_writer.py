import serial
import csv
import datetime
import time

arduino = serial.Serial('/dev/ttyACM1', 9600)
print("inicia recepción de datos serial")
i=0
while 1:
	now = datetime.datetime.now()
	if(arduino.in_waiting >0):
		time.sleep(1)
		line = str(arduino.readline())[2:-5]
		if line == "1999":
			print("recepcion")
			print(i)
			i+=1
			temp = str(arduino.readline())[2:-5]
			lvl_f = str(arduino.readline())[2:-5]
			hum = str(arduino.readline())[2:-5]
			luz = str(arduino.readline())[2:-5]
			now = now.strftime("%M.%S")
			with open('data.csv', 'a') as csvFile:
				row=[]
				writer = csv.writer(csvFile)
				
				writer.writerow([temp,lvl_f,hum,luz,now])


