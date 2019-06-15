import paramiko
from scp import SCPClient

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect("192.168.0.17", "22", "ubuntu", "87023131")
    return client

ssh = createSSHClient("192.168.0.17", "22", "ubuntu", "87023131")
scp = SCPClient(ssh.get_transport())

scp.get(r'/home/ubuntu/data.csv')
scp.get(r'/home/ubuntu/humedad.png')
scp.get(r'/home/ubuntu/luz.png')
scp.get(r'/home/ubuntu/nivel.png')
scp.get(r'/home/ubuntu/temper.png')
scp.put(r'/home/thor/Escritorio/telegram_bot/telegram-bot/variables.py')