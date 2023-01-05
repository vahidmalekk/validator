import requests
import subprocess
import time

baner = '''                                 z11                               
                                   z@d                               
                                    0@@.                z@.          
                                   z1jd01j".          j11j           
                                  110jd@z@000@jjjjjz@1jd.            
                                zj@j @jd    "zzzzzj@0dz0             
jdd@j1""                    "zj@d@.   00z       .jjd1 @@             
  "z11j@00jjjzz   .zzzz"zjj00@1z.   .111@01jz".zj10.  110            
         """j1j1jzzz10j11z""      .zj@0@0@j1j@1@1@j   .@1@           
             .j@@""j1000@11111111@0@11@1j@00@@@01@0     1d0"         
              "@d.     jjd11@0@@dd@1@dd1jd0@1d0@zj10z    z@@0z       
               z00      00"   @1d110@d0@0@1@@j@j0@1@d@11111@1@@111@@@
                1@j     j0.   "@d   "j0@01j0jjjd1@@dddjzzzzz0@dj"    
                j@@     j0.   11d"j10@@@1d@1dz10?zz00.     z@0j      
                j@d"   z?0. .j@100@j   j11 jj0?@1"@d"     .@@"       
                z01   z1@jj@@d@1.     "@0z  "z1@0d1j      011        
               1z0. "@0d@@@110z"      d@d    .@j@d0j     j1@         
              0@0 .j@1jjj"  "zj@11"  .d?zzj10@@@0@jd     0@z         
            "??d1j@@0@1.       .z@@010@00@1".    @@@0.   @d          
           1@000@11j100dd0@11z.    z1@d0111@01111j0@0d   @d          
        .j@0@?0@zzz.      "zz@d1"   1ddd0@""""""zzj@00d. d?          
     zj0d011111jzj0000@11z.   z0d0" 0z10.           .100"0dj         
 "z10@@j.             .zz10@1   "0d?zj1               j@dd@@         
@@vahid                     z10dj   00@1    ..zj"1@zzzj".j@000z        
                            zdd@  11@  "z001jjjjjjzzj1100111d        
                             .1??j0@1z0d@.               zzzj@       
                               j?d1010@.                   .1@@"     
                                jz00j                        jd?"    
                                jj@                           .d01   
                               .11j                             j@0" 
                               j@0                               zj1 
                               j0j'''
def banner():
    subprocess.run(["clear"])
    print(baner)
    print("=================================================================================")
    print("=================================================================================")
    print("im looking for parametrs")




def spider(domain):
     subprocess.run(["rm", "-f", "param"])
     valid=[]
     url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=txt&fl=original&collapse=urlkey&page=/"
     wayback=requests.get(url)
     text = wayback.text.split("\n")
     for i in text:
         if "=" in i:
             valid.append(i)

     parametr(valid)




def parametr(li):

    for i in li:
        alll = i.split("/")[-1]
        ll = alll.split("?")
        bo = i.split("?")[0]
        body = bo.split("/")[-1]
        qus = alll.split("?")[-1]
        param = qus.split("&")

        file = open("param","a")
        for pp in param:
            xxx = pp.split("=")[-1]
            ja = param.index(pp)
            param[ja] = pp.split("=")[0] + "=" + "RFUZZ"
            if len(param) > 1:
               final_a= i.split("?")[0] + "?" + "&".join(param)
               file.write(final_a+"\n")
            else:
                final_b= i.split("?")[0] + "?" + "&".join(param)
                file.write(final_b+"\n")

            param[ja] = pp.split("=")[0] + "=" + xxx
        file.close()


banner()





