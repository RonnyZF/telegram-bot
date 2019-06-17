from pexpect import pxssh

s=pxssh.pxssh()

if not s.login('192.168.0.18','ubuntu','87023131'):
	print("SSH session failed on login")

else:
	print("SSH session login successtul")
	s.sendline('cd /home/ubuntu/Desktop/telegram-bot')
	s.sendline("python3 -c 'import arduinoCtrl; arduinoCtrl.write_varFile([9,6,7])'")
	s.prompt()
	print (s.before)
	s.logout()