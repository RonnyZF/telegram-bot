#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os, sys
import serial
import csv
import variables

arduino = serial.Serial('/dev/ttyACM1', 9600)

def controlar_luces():
	arduino.write(str.encode("L"))

def controlar_ventiladores():
	arduino.write(str.encode("V"))

def controlar_cortinas():
	arduino.write(str.encode("C"))

def encender_luces():
	variables.luces='ON'
	arduino.write(str.encode("I"))		

def apagar_luces():
	variables.luces='OFF'
	arduino.write(str.encode("O"))

def encender_ventiladores():
	variables.ventiladores='ON'
	arduino.write(str.encode("I"))		

def apagar_ventiladores():
	variables.ventiladores='OFF'
	arduino.write(str.encode("O"))

def cortinas_cerradas():
	variables.cortinas='cerradas'
	arduino.write(str.encode("0"))

def cortinas_20():
	variables.cortinas='20% abiertas'
	arduino.write(str.encode("1"))

def cortinas_40():
	variables.cortinas='40% abiertas'
	arduino.write(str.encode("2"))

def cortinas_60():
	variables.cortinas='60% abiertas'
	arduino.write(str.encode("3"))

def cortinas_80():
	variables.cortinas='80% abiertas'
	arduino.write(str.encode("4"))

def cortinas_100():
	variables.cortinas='100% abiertas'
	arduino.write(str.encode("5"))		

def lectura_sensores():
	arduino.write(str.encode("S"))

def display_sensor_data():
	with open('data.csv', 'r') as csv_file:
		data=list(csv.reader(csv_file))[-1]
	data.extend([variables.luces,variables.ventiladores,variables.cortinas])
	return data

