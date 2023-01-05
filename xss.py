#!/usr/bin/env python3
import requests as req

import urllib.parse

def xss():
    xss_list=["q=",
"s=",
"search=",
"lang=",
"keyword=",
"query=",
"page=",
"keywords=",
"year=",
"view=",
"email=",
"type=",
"name=",
"p=",
"callback=",
"jsonp=",
"api_key=",
"api=",
"password=",
"email=",
"emailto=",
"token=",
"username=",
"csrf_token=",
"unsubscribe_token=",
"id=",
"item=",
"page_id=",
"month=",
"immagine=",
"list_type=",
"url=",
"terms=",
"categoryid=",
"key=",
"l=",
"begindate=",
"enddate="
]
    valid_parma=[]
    def req_rep():

        print(f"wait {len(valid_parma)} links are testing for possible paramters for xss!!!")
        for url in valid_parma:
            try:
                send = req.get(f"{urllib.parse.quote(url.strip())}")
                answer = str(send.text)
                if "RFUZZ" in answer:
                    print("possible for xss -> " + url)
            except:
                pass
    ###############################################################
    file = open("param", "r")
    for i in file.readlines():
        for param in xss_list:
            if param in i:
                valid_parma.append(i)


    req_rep()
    file.close()

