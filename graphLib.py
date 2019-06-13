
import datetime
import csv
import itertools
import matplotlib.pyplot as plt

now = datetime.datetime.now()
tiempo=[]
temperatura=[]
humedad=[]
distancia=[]
luminosidad=[]


def graficar_temp():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print (row)
            temp=float(row[0])
            time=float(row[5])
            temperatura.append(temp)
            tiempo.append(time)
 
    fig1=plt.figure(1)
    plt.plot(tiempo,temperatura, 'm')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Temperatura (C)')
    plt.title('Temperatura')
    plt.grid(True)
    plt.savefig("temper.png")
    plt.show()


def graficar_hum():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[5])
            humed=float(row[0])
            tiempo.append(time)
            humedad.append(humed)
    fig2=plt.figure(2)
    plt.plot(tiempo,humedad, 'm') ####****
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Humedad ')
    plt.title('Humedad vs Tiempo')
    plt.grid(True)
    plt.savefig("humedad.png")
    plt.show()



def graficar_nivel():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[5])
            dist=floar(row[0])
            tiempo.append(time)
            distancia.append(dist)
    fig3=plt.figure(3)
    plt.plot(tiempo,distancia, 'm')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Nivel ')
    plt.title('Nivel de alimento')
    plt.grid(True)
    plt.savefig("nivel.png")
    plt.show()



def graficar_luminosidad():

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[5])
            lum=float(row[0])
            tiempo.append(time)
            luminosidad.append(lum)
    fig4=plt.figure(4)
    plt.plot(tiempo,luminosidad, 'm')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Luminosidad ')
    plt.title('Luminosidad')
    plt.grid(True)
    plt.savefig("luz.png")
    plt.show()



graficar_luminosidad()

#graficar_hum()



#graficar_nivel()



#graficar_temp()
