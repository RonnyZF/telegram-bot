
import datetime
import csv
import itertools
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.signal as signal

now = datetime.datetime.now()

def graficar_temp():
    tiempo=[]
    temperatura=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            temp=float(row[0])
            time=float(row[4])
            temperatura.append(temp)
            tiempo.append(time)
 
    fig1=plt.figure(1)
    ax = fig1.add_subplot(1, 1, 1)
    axes = plt.gca()
    axes.set_xlim([0,24])
    axes.set_ylim([0,30])
    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 23.1, 1)
    minor_ticks = np.arange(0, 23.1, 0.5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
#    ax.set_yticks(major_ticks)
#    ax.set_yticks(minor_ticks, minor=True)
    plt.plot(tiempo,temperatura, 'm')
    plt.xlabel('Tiempo (horas)')
    plt.ylabel('Temperatura (C)')
    plt.title('Temperatura')
    plt.grid(True)
    plt.savefig("graphT.png")
    #plt.show()

def graficar_nivel():
    tiempo=[]
    distancia=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[4])
            dist=float(row[1])
            tiempo.append(time)
            distancia.append(dist)
    distancia_f=sp.signal.medfilt(distancia,21)
    print(len(tiempo))
    print(len(distancia_f))
    fig3=plt.figure(3)
    ax = fig3.add_subplot(1, 1, 1)
    axes = plt.gca()
    axes.set_xlim([0,24])
    axes.set_ylim([0,100])
    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 23.1, 1)
    minor_ticks = np.arange(0, 23.1, 0.5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
#    ax.set_yticks(major_ticks)
#    ax.set_yticks(minor_ticks, minor=True)
    plt.plot(tiempo,distancia_f, 'm')
    plt.xlabel('Tiempo (horas)')
    plt.ylabel('Porcentaje nivel de alimento')
    plt.title('Nivel de alimento')
    plt.grid(True)
    plt.savefig("graphA.png")
    #plt.show()



def graficar_hum():
    tiempo=[]
    humedad=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[4])
            humed=float(row[2])
            tiempo.append(time)
            humedad.append(humed)
    fig2=plt.figure(2)
    ax = fig2.add_subplot(1, 1, 1)
    axes = plt.gca()
    axes.set_xlim([0,24])
    axes.set_ylim([0,100])
    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 23.1, 1)
    minor_ticks = np.arange(0, 23.1, 0.5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
#    ax.set_yticks(major_ticks)
#    ax.set_yticks(minor_ticks, minor=True)
    plt.plot(tiempo,humedad,'m')
    plt.xlabel('Tiempo (horas)')
    plt.ylabel('Humedad ')
    plt.title('Humedad vs Tiempo')
    plt.grid(True)
    plt.savefig("graphH.png")
    #plt.show()

def graficar_luminosidad():
    tiempo=[]
    luminosidad=[]
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[4])
            lum=float(row[3])
            tiempo.append(time)
            luminosidad.append(lum)
    fig4=plt.figure(4)
    ax = fig4.add_subplot(1, 1, 1)
    axes = plt.gca()
    axes.set_xlim([0,24])
    axes.set_ylim([0,100])
    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 23.1, 1)
    minor_ticks = np.arange(0, 23.1, 0.5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
#    ax.set_yticks(major_ticks)
#    ax.set_yticks(minor_ticks, minor=True)
    plt.plot(tiempo,luminosidad, 'm')
    plt.xlabel('Tiempo (horas)')
    plt.title('Luminosidad')
    plt.grid(True)
    plt.savefig("luz.png")
    #plt.show()



graficar_temp()
graficar_nivel()
graficar_hum()
graficar_luminosidad()



