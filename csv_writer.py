import serial
import csv

arduino = serial.Serial('/dev/ttyACM0', 9600)
while 1:
	if(arduino.in_waiting >0):
		line = str(arduino.readline())[2:-5]
		if line == "1999":
			temp = str(arduino.readline())[2:-5]
			lvl_f = str(arduino.readline())[2:-5]
			hum = str(arduino.readline())[2:-5]
			luz = str(arduino.readline())[2:-5]
			now = datetime.datetime.now().minute
			with open('data.csv', 'a') as csvFile:
				row=[]
				writer = csv.writer(csvFile)
				
				writer.writerow([temp,lvl_f,hum,luz,now])


