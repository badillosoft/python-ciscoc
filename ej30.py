import paramiko
from getpass import getpass

host = "10.102.94.110"
username = "pi" # raw_input("User: ")
password = "raspberry" # getpass("Password: ")

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for i in range(3):
    try:
        ssh.connect(host, username=username, password=password)
        break
    except:
        print "Invalid user or password (%d)" % i

if i == 2:
    print "Can't connect :("
    exit()

print "Connected"

stdin, stdout, stderr = ssh.exec_command("cat conversaciones.txt")
conversaciones = stdout.readlines()

ssh.close()

text = "".join(conversaciones)

print text

import re

pattern = "(\d{4}[\-\s\t]?){4}"

for m in re.finditer(pattern, text):
    card = m.group(0)
    print "Tarjeta: %s" % card