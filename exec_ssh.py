from pexpect import pxssh

def controlar_luces():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.controlar_luces()'")
		s.prompt()
		print (s.before)
		s.logout()

def controlar_ventiladores():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.controlar_ventiladores()'")
		s.prompt()
		print (s.before)
		s.logout()	

def controlar_cortinas():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.controlar_cortinas()'")
		s.prompt()
		print (s.before)
		s.logout()	

def encender_luces():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.encender_luces()'")
		s.prompt()
		print (s.before)
		s.logout()	

def apagar_luces():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.apagar_luces()'")
		s.prompt()
		print (s.before)
		s.logout()

def encender_ventiladores():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.encender_ventiladores()'")
		s.prompt()
		print (s.before)
		s.logout()

def apagar_ventiladores():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.apagar_ventiladores()'")
		s.prompt()
		print (s.before)
		s.logout()

def cortinas_cerradas():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.cortinas_cerradas()'")
		s.prompt()
		print (s.before)
		s.logout()

def cortinas_20():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.cortinas_20()'")
		s.prompt()
		print (s.before)
		s.logout()

def cortinas_40():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.cortinas_40()'")
		s.prompt()
		print (s.before)
		s.logout()

def cortinas_60():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.cortinas_60()'")
		s.prompt()
		print (s.before)
		s.logout()

def cortinas_80():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.cortinas_80()'")
		s.prompt()
		print (s.before)
		s.logout()

def cortinas_100():
	s=pxssh.pxssh()
	if not s.login('192.168.0.18','ubuntu','87023131'):
		print("SSH session failed on login")
	else:
		print("SSH session login successtul")
		s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
		s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.cortinas_100()'")
		s.prompt()
		print (s.before)
		s.logout()	