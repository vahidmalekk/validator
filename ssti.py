#!/usr/bin/env python3
import requests as req
import urllib.parse

ssti=["{{85*85}}","${85*85}","<%= 85*85 %>","${{85*85}}","#{85*85}"]

def ssti(file):
    ssti = ["{{85*85}}", "${85*85}", "<%= 85*85 %>", "${{85*85}}", "#{85*85}"]
    file = open(file, "r")
    for i in file.readlines():
        for j in ssti:
            ready = i.replace("RFUZZ", j)
            read = urllib.parse.quote(ready)

            try:
                send = req.get(f"{read}")
                answer = str(send.text)
                if "7225" in answer:
                    print(ready)
            except:
                pass
    file.close()


