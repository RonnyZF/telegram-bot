from pexpect import pxssh

s=pxssh.pxssh()

if not s.login('192.168.0.18','ubuntu','87023131'):
	print("SSH session failed on login")

else:
	print("SSH session login successtul")
	s.sendline('uptime')
	s.prompt()
	print (s.before)
	s.logout()