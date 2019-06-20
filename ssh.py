import paramiko
import sys

nbytes = 4096
hostname = '192.168.0.34'
port = 22
username = 'pi' 
password = 'raspberry'
command = 'ls'
cmd='ls' 

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname,port,username,password)

stdin,stdout,stderr=ssh.exec_command(cmd)
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)
