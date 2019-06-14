
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
            temp=float(row[0])
            time=float(row[4])
            temperatura.append(temp)
            tiempo.append(time)
 
    fig1=plt.figure(1)
    plt.plot(tiempo,temperatura, 'm')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Temperatura (C)')
    plt.title('Temperatura')
    plt.grid(True)
    plt.savefig("graphT.png")
    #plt.show()

def graficar_nivel():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[4])
            dist=float(row[1])
            #tiempo.append(time)
            distancia.append(dist)
    print(len(tiempo))
    print(len(distancia))
    fig3=plt.figure(3)
    plt.plot(tiempo,distancia, 'm')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Nivel ')
    plt.title('Nivel de alimento')
    plt.grid(True)
    plt.savefig("graphA.png")
    #plt.show()



def graficar_hum():
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[4])
            humed=float(row[2])
            #tiempo.append(time)
            humedad.append(humed)
    fig2=plt.figure(2)
    plt.plot(tiempo,humedad,'m')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Humedad ')
    plt.title('Humedad vs Tiempo')
    plt.grid(True)
    plt.savefig("graphH.png")
    #plt.show()

def graficar_luminosidad():

    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            time=float(row[4])
            lum=float(row[3])
            #tiempo.append(time)
            luminosidad.append(lum)
    fig4=plt.figure(4)
    plt.plot(tiempo,luminosidad, 'm')
    plt.xlabel('Tiempo (s)')
    plt.title('Luminosidad')
    plt.grid(True)
    plt.savefig("luz.png")
    #plt.show()



#graficar_temp()
#graficar_nivel()
#graficar_hum()
#graficar_luminosidad()



