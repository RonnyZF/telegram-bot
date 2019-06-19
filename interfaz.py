from paramiko import *
from scp import SCPClient
from tkinter import *
from tkinter import ttk
from PIL import Image
import csv
from exec_ssh import *

#Datos de lectura de sensores

Fecha = "18/06/2019"
Hora = 0
Tem = 0
humedad = 0
nal = 0
nluz = 0
ecort = 10
event = 10
eluz = 10

eventv = 'NOT'
eluzv = 'NOT'
ecortv = 'NOT'
#Datos de control
v_l = 0
v_c = 0
v_v = 0

puerto='172.21.236.108'

#Ubicaciones de graficas
Ub_logo = "21"
Ub_grafhum = "graphH.png"
Ub_graflum = "graphT.png"
Ub_graftemp = "graphT.png"
Ub_grafniv = "graphA.png"

class Aplicacion():
	def __init__(self):  
        	self.raiz = Tk()
        	self.raiz.attributes('-fullscreen',True)
        	#self.raiz.attributes('-topmost', True)
        	#self.raiz.geometry('500x430')
        	self.raiz.geometry("{0}x{1}+0+0".format(self.raiz.winfo_screenwidth(), self.raiz.winfo_screenheight()))   
        	self.raiz.resizable(width=True,height=True)
        	self.raiz.title('PouCOMS')


        	self.image = Text(self.raiz,width=57,heigh=11)
        	
        	#self.image.pack(expand=True,fill=BOTH)
        	self.image.pack(side=TOP)
        	


        	self.binfo = ttk.Button(self.raiz, text='Info', 
                                	command=self.verinfo)                        
        	#self.binfo.place(x=10,y=200)
        	self.binfo.pack()
        	
        	self.breturn = ttk.Button(self.raiz,text='Refrescar',
        							 command=self.ret)
        	#self.breturn.place(x=300, y=200)
        	self.breturn.pack()

        	self.bgraf = ttk.Button(self.raiz,text='graficas',
        							 command=self.grafi)
        	#self.bgraf.place(x=205, y=200)
        	self.bgraf.pack()

        	self.bctrl = ttk.Button(self.raiz,text='Control',
        							 command=self.ctrl)
        	#self.bctrl.place(x=105, y=200)
        	self.bctrl.pack()

        	self.bsalir = ttk.Button(self.raiz, text='Salir',
 									command=self.raiz.destroy)         
        	#elf.bsalir.place(x=400,y= 200)
        	self.bsalir.pack()

        	self.tinfo = Text(self.raiz, width=57, height=11)
        	#self.tinfo.pack(side=BOTTOM)
        	self.tinfo.pack()
        	#self.tinfo.pack(expand=True) 

        	imagen = PhotoImage(file = "logoA.png")
        	fondo = Label(self.image,image=imagen).pack(expand=True)

        	self.binfo.focus_set()
        	self.raiz.mainloop()
	

	def var_cam(self):
		global eluzv, ecortv, eventv
		if (int(eluz)==1): 
			eluzv ='ON'
		elif eluz =='0': eluzv = 'OFF'
		if event == '1': eventv = 'ON'
		elif event =='0': eventv = 'OFF'
		if ecort =='0': ecortv = 'Cerradas'
		elif ecort=='1': ecortv = '20% abuertas'
		elif ecort=='2': ecortv = '40% abuertas'
		elif ecort=='3': ecortv = '60% abuertas'
		elif ecort=='4': ecortv = '80% abuertas'
		elif ecort=='5': ecortv = 'Abiertas'

	def verinfo(self):
			self.var_cam()
			self.tinfo.delete("1.0", END)
			texto_info = "Información de sensores"+ "\n"
			texto_info += "Fecha: " + Fecha + " Hora: " + str(Hora) + "\n"
			texto_info += "Temperatura actual: " + str(Tem) + "°C"+ "\n"
			texto_info += "Humedad actual: " + str(humedad) + "%"+ "\n"
			texto_info += "Nivel de luz:" + str(nluz) + "%" + "\n"
			texto_info += "Nivel Alimento: " + str(nal) +"%"+ "\n"
			texto_info += "Estado de las luces:" + eluzv + "\n"
			texto_info += "Estado de los ventiladores: " + str(eventv) + "\n"
			texto_info += "Estado de Cortinas: " + str(ecortv) + "\n"
			self.tinfo.insert("1.0", texto_info)

	def ret(self):
		server_leer()
		leer_archivo()
		leer_archivo2()

	def ctrl(self):
		control()


	def grafi(self):
		Grafic()

	
class control():
	def __init__(self):   
        	self.raizc = Toplevel()
        	self.raizc.geometry('475x260')   
        	self.raizc.resizable(width=False,height=False)
        	self.raizc.title('PouCOMS')


        	self.imagec = Text(self.raizc,width=475,heigh=260)
        	self.imagec.pack(side=BOTTOM)

        	self.bsalir = ttk.Button(self.raizc, text='Regresar',
 									command=self.raizc.destroy)         
        	self.bsalir.place(x=375,y= 5)
        	

        	self.bctrlluz = ttk.Button(self.raizc, text='Control Luces', 
									command=self.ctrlluz)
        	self.bctrlluz.place(x=15,y=5)

        	self.bctrlcort = ttk.Button(self.raizc, text='Control cortinas', 
									command=self.ctrlcortinas)
        	self.bctrlcort.place(x=115,y=5)

        	self.bctrlventiladores = ttk.Button(self.raizc, text='Control ventiladores', 
									command=self.ctrlventiladores)
        	self.bctrlventiladores.place(x=230,y=5)

        	imagenc = PhotoImage(file = "logoA.png")
        	fondo2 = Label(self.imagec,image=imagenc).place(x=10,y=40)

        	self.raizc.mainloop()

	def ctrlluz(self):

		self.bcrtluzenc = ttk.Button(self.raizc, text='Encender',
									command=self.crtluzenc)
		self.bcrtluzenc.place(x=15, y= 40)


		self.bcrtluzapg = ttk.Button(self.raizc, text='Apagar',
									command=self.crtluzapg)
		self.bcrtluzapg.place(x=15, y= 80)


	def ctrlcortinas(self):

		self.bcrtcortcer = ttk.Button(self.raizc, text='Cerrado',
									command=self.crtcortcer)
		self.bcrtcortcer.place(x=123, y= 40)

		self.bcrtcort20 = ttk.Button(self.raizc, text='Apertura 20',
									command=self.crtcort20)
		self.bcrtcort20.place(x=120, y= 75)

		self.bcrtcort40 = ttk.Button(self.raizc, text='Apertura 40',
									command=self.crtcort40)
		self.bcrtcort40.place(x=120, y= 115)

		self.bcrtcort60 = ttk.Button(self.raizc, text='Apertura 60',
									command=self.crtcort60)
		self.bcrtcort60.place(x=120, y= 155)

		self.bcrtcort80 = ttk.Button(self.raizc, text='Apertura 80',
									command=self.crtcort80)
		self.bcrtcort80.place(x=120, y= 195)

		self.bcrtcortabr = ttk.Button(self.raizc, text='Abiertas',
									command=self.crtcortabr)
		self.bcrtcortabr.place(x=123, y= 230)


	def ctrlventiladores(self):

		self.bcrtventenc = ttk.Button(self.raizc, text='Encender',
									command=self.crtventenc)
		self.bcrtventenc.place(x=255, y= 40)

		self.bcrtventapg =ttk.Button(self.raizc, text='Apagar',
									command=self.crtventapg)
		self.bcrtventapg.place(x=255, y = 80)




	def crtluzenc(self):
		global v_l
		v_l = 1
		escribir_archivo()
		controlar_luces()
		encender_luces()

	def crtluzapg(self):
		global v_l
		v_l = 0
		escribir_archivo()
		controlar_luces()
		apagar_luces()

	def crtcortcer(self):
		global v_c
		v_c = 0
		escribir_archivo()
		controlar_cortinas()
		cortinas_cerradas()


	def crtcort20(self):
		global v_c
		v_c = 1
		escribir_archivo()
		controlar_cortinas()
		cortinas_20()

	def crtcort40(self):
		global v_c
		v_c = 2
		escribir_archivo()
		controlar_cortinas()
		cortinas_40()

	def crtcort60(self):
		global v_c
		v_c = 3
		escribir_archivo()
		controlar_cortinas()
		cortinas_60()

	def crtcort80(self):
		global v_c
		v_c = 4
		escribir_archivo()
		controlar_cortinas()
		cortinas_80()

	def crtcortabr(self):
		global v_c
		v_c = 5
		escribir_archivo()
		controlar_cortinas()
		cortinas_100()

	def crtventenc(self):
		global v_v
		v_v = 1
		escribir_archivo()
		controlar_ventiladores()
		encender_ventiladores()

	def crtventapg(self):
		global v_v
		v_v = 0
		escribir_archivo()
		controlar_ventiladores()
		apagar_ventiladores()

class Grafic():
	def __init__(self):   
        	self.raizg = Toplevel()
        	self.raizg.geometry('475x260')   
        	self.raizg.resizable(width=False,height=False)
        	self.raizg.title('PouCOMS')
        	self.imageg = Text(self.raizg,width=475,heigh=260)
        	self.imageg.pack(side=BOTTOM)
        	

        	self.bhum = ttk.Button(self.raizg, text='Humedad',
 									command=self.grafhum)         
        	self.bhum.place(x=0,y= 0)

        	self.bnival = ttk.Button(self.raizg, text='Nivel Alimento',
 									command=self.grafnival)         
        	self.bnival.place(x=85,y= 0)

        	self.blum = ttk.Button(self.raizg, text='Luminosidad',
 									command=self.graflum)         
        	self.blum.place(x=195,y= 0)

        	self.btemp = ttk.Button(self.raizg, text='Temperatura',
 									command=self.graftemp)         
        	self.btemp.place(x=290,y= 0)


        	self.bsalir = ttk.Button(self.raizg, text='Regresar',
 									command=self.raizg.destroy)         
        	self.bsalir.place(x=385,y= 0)

        	imageng = PhotoImage(file = "logoA.png")
        	fondo2 = Label(self.imageg,image=imageng).place(x=10,y=40)

        	self.raizg.mainloop()
	def grafhum(self):
		Grafh()
		self.raizg.delete("1.0",END)

	def graflum(self):
		Grafl()
		self.raizg.delete("1.0",END)

	def grafnival(self):
		Grafn()
		self.raizg.delete("1.0",END)

	def graftemp(self):
		Graft()
		self.raizg.delete("1.0",END)

class Grafh():
	def __init__(self):   
        	self.raizh = Toplevel()
        	self.raizh.geometry('600x480')   
        	self.raizh.resizable(width=False,height=False)
        	self.raizh.title('PouCOMS')
        	self.imageh = Text(self.raizh,width=500,heigh=400)
        	self.imageh.pack(side=BOTTOM)

        	self.bsalir = ttk.Button(self.raizh, text='Regresar',
 									command=self.raizh.destroy)         
        	self.bsalir.place(x=290,y= 5)
        	imagenh = PhotoImage(file = Ub_grafhum)
        	fondo2 = Label(self.imageh,image=imagenh).place(x=0,y=0)

        	self.raizh.mainloop()

class Grafn():
	def __init__(self):   
        	self.raizn = Toplevel()
        	self.raizn.geometry('600x480')   
        	self.raizn.resizable(width=False,height=False)
        	self.raizn.title('PouCOMS')
        	self.imagen = Text(self.raizn,width=500,heigh=400)
        	self.imagen.pack(side=BOTTOM)

        	self.bsalir = ttk.Button(self.raizn, text='Regresar',
 									command=self.raizn.destroy)         
        	self.bsalir.place(x=290,y= 5)
        	imagenn = PhotoImage(file = Ub_grafniv)
        	fondo2 = Label(self.imagen,image=imagenn).place(x=0,y=0)

        	self.raizn.mainloop()

class Grafl():
	def __init__(self):   
        	self.raizl = Toplevel()
        	self.raizl.geometry('600x480')   
        	self.raizl.resizable(width=False,height=False)
        	self.raizl.title('PouCOMS')
        	self.imagel = Text(self.raizl,width=500,heigh=400)
        	self.imagel.pack(side=BOTTOM)

        	self.bsalir = ttk.Button(self.raizl, text='Regresar',
 									command=self.raizl.destroy)         
        	self.bsalir.place(x=290,y= 5)
        	imagenl = PhotoImage(file = Ub_graflum)
        	fondo2 = Label(self.imagel,image=imagenl).place(x=0,y=0)

        	self.raizl.mainloop()

class Graft():
	def __init__(self):   
        	self.raizt = Toplevel()
        	self.raizt.geometry('600x480')   
        	self.raizt.resizable(width=False,height=False)
        	self.raizt.title('PouCOMS')
        	self.imaget = Text(self.raizt,width=500,heigh=400)
        	self.imaget.pack(side=BOTTOM)

        	self.bsalir = ttk.Button(self.raizt, text='Regresar',
 									command=self.raizt.destroy)         
        	self.bsalir.place(x=290,y= 5)
        	imagent = PhotoImage(file = Ub_graftemp)
        	fondo2 = Label(self.imaget,image=imagent).place(x=0,y=0)

        	self.raizt.mainloop()

def server_leer():
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(AutoAddPolicy)
	ssh.connect(hostname=puerto,username='pi',password='0117')
	#SCPCLient takes a paramiko transport as an argument
	scp= SCPClient(ssh.get_transport())
	scp.get(r'/home/pi/project/telegram-bot/data.csv')
	scp.get(r'/home/pi/project/telegram-bot/graphH.png')
	scp.get(r'/home/pi/project/telegram-bot/graphA.png')
	scp.get(r'/home/pi/project/telegram-bot/graphA.png')
	scp.get(r'/home/pi/project/telegram-bot/graphT.png')
	scp.get(r'/home/pi/project/telegram-bot/variables.csv')
	scp.close()

def server_escribir():
	ssh = SSHClient()
	ssh.load_system_host_keys()
	ssh.set_missing_host_key_policy(AutoAddPolicy)
	ssh.connect(hostname=puerto,username='pi',password='0117')
	#SCPCLient takes a paramiko transport as an argument
	scp= SCPClient(ssh.get_transport())
	scp.put(r'variables.csv',remote_path='/home/pi/project/telegram-bot')
	#stdin, stdout, stderr = ssh.exec_command('cd /home/pi/project/telegram-bot; rm nuevo.txt')
	scp.close()

def leer_archivo():
	with open('data.csv') as File:
		reader = csv.reader(File,delimiter=',', quotechar =',',
							quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			dat=row
		global Hora, Tem, humedad, nal,nluz
		Hora = dat[4]
		Tem = dat[0]
		humedad = dat[2]
		nal = dat[1]
		nluz = dat[3]

def leer_archivo2():
	with open('variables.csv') as File:
		reader = csv.reader(File,delimiter=',', quotechar =',',
							quoting=csv.QUOTE_MINIMAL)
		for row in reader:
			date=row
		global ecort, event, eluz
		ecort = date[2]
		eluz = date[0]
		event = date[1]
		print(date)


def escribir_archivo():
	with open('variables.csv', mode = 'w+') as variables:
		variables_write = csv.writer(variables,delimiter = ',', quotechar='"',
			quoting = csv.QUOTE_MINIMAL)
		variables_write.writerow([v_l,v_v,v_c])
	server_escribir()


def main():
	mi_app = Aplicacion()
	return 0
if __name__ == '__main__':
	main()
