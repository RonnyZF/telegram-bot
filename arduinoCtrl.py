#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
import serial
import csv

arduino = serial.Serial('/dev/ttyACM1', 9600)

def controlar_luces():
	arduino.write(str.encode("L"))

def controlar_ventiladores():
	arduino.write(str.encode("V"))

def controlar_cortinas():
	arduino.write(str.encode("C"))

def encender_luces():
	ctrl=read_varFile()
	ctrl[0]=1
	write_varFile(ctrl)
	arduino.write(str.encode("I"))		

def apagar_luces():
	ctrl=read_varFile()
	ctrl[0]=0
	write_varFile(ctrl)
	arduino.write(str.encode("O"))

def encender_ventiladores():
	ctrl=read_varFile()
	ctrl[1]=1
	write_varFile(ctrl)
	arduino.write(str.encode("I"))		

def apagar_ventiladores():
	ctrl=read_varFile()
	ctrl[1]=0
	write_varFile(ctrl)
	arduino.write(str.encode("O"))

def cortinas_cerradas():
	ctrl=read_varFile()
	ctrl[2]=0
	write_varFile(ctrl)
	arduino.write(str.encode("0"))

def cortinas_20():
	ctrl=read_varFile()
	ctrl[2]=1
	write_varFile(ctrl)
	arduino.write(str.encode("1"))

def cortinas_40():
	ctrl=read_varFile()
	ctrl[2]=2
	write_varFile(ctrl)
	arduino.write(str.encode("2"))

def cortinas_60():
	ctrl=read_varFile()
	ctrl[2]=3
	write_varFile(ctrl)
	arduino.write(str.encode("3"))

def cortinas_80():
	ctrl=read_varFile()
	ctrl[2]=4
	write_varFile(ctrl)
	arduino.write(str.encode("4"))

def cortinas_100():
	ctrl=read_varFile()
	ctrl[2]=5
	write_varFile(ctrl)
	arduino.write(str.encode("5"))		

def lectura_sensores():
	arduino.write(str.encode("S"))

def display_sensor_data():
	with open('data.csv', 'r') as csv_file:
		data=list(csv.reader(csv_file))[-1]
	ctrl=read_varFile()
	luces=""
	ventiladores=""
	cortinas=""
	if ctrl[0]==1: luces="ON"
	elif ctrl[0]==0: luces= "OFF"

	if ctrl[1]==1: ventiladores="ON"
	elif ctrl[1]==0: ventiladores= "OFF"

	if ctrl[2]==0: cortinas="Cerradas"
	elif ctrl[2]==1: cortinas= "20% abiertas"
	elif ctrl[2]==2: cortinas= "40% abiertas"
	elif ctrl[2]==3: cortinas= "60% abiertas"
	elif ctrl[2]==4: cortinas= "80% abiertas"
	elif ctrl[2]==5: cortinas= "100% abiertas"
	data.extend([luces,ventiladores,cortinas])
	return data

def read_varFile():
	with open('variables.csv') as varFile:
		csv_reader= csv.reader(varFile, delimiter=',')
		for row in csv_reader:
			c_l=int(row[0])
			c_v=int(row[1])
			c_c=int(row[2])
	ctrl=[c_l,c_v,c_c]
	return ctrl

def write_varFile(ctrl):
	with open('variables.csv','w') as varFile:
		writer=csv.writer(varFile)
		writer.writerow([ctrl[0],ctrl[1],ctrl[2]])

