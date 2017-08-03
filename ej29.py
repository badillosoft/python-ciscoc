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

stdin, stdout, stderr = ssh.exec_command("pwd")
print stdout.readlines()

stdin, stdout, stderr = ssh.exec_command("mkdir foo")
print stdout.readlines(), stderr.readlines()

stdin, stdout, stderr = ssh.exec_command("ls")
print stdout.readlines()

stdin, stdout, stderr = ssh.exec_command('echo "print \'hola soy script\'" > foo/script.py')
print stdout.readlines(), stderr.readlines()

stdin, stdout, stderr = ssh.exec_command('python foo/script.py')
print stdout.readlines(), stderr.readlines()

ssh.close()