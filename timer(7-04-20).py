import time
import os
import speech_recognition as sr
import re 
import json
import sys
import threading
import pyttsx3
#import playsound
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)



def check(hour,min,sec,name=" "): 
    H = str (hour)
    M = str (min)
    S = str (sec) 
    N = str (name)
    c= ":"
    #print("file name is :", name)
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-50)
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[1].id) 
    if H != "0" and M !="0" and S !="0":
        filename=H+" hour "+M+" minutes "+S+" seconds "
    if H == "0" and M !="0" and S !="0":
        filename=M+" minutes "+S+" seconds "
    if H == "0" and M =="0" and S !="0":
        filename=S+" seconds "
    if H != "0" and M !="0" and S =="0":
        filename=H+" hour "+M+" minutes "
    if H == "0" and M !="0" and S =="0": # m
        filename=M+" minutes "
    if H != "0" and M =="0" and S == "0":
        filename=H+ " hour "
    

    while hour > -1:
        while min > -1:
            while sec > 0:
                sec=sec-1
                time.sleep(1)
                sec1 = ('%02.f' % sec)  
                min1 = ('%02.f' % min)
                hour1 = ('%02.f' % hour)
                sys.stdout.write('\r' + str(hour1) + c + str(min1) + c + str(sec1))
                log=str(str(hour1) +" hours "+  str(min1) +  " Minutes " + str(sec1) + " seconds"+ " is remaining")

                def log1(Lname,filename,log):

                    if name != ' ':
                            f=open(Lname+".txt",'w')
                            f.write(log)
                    if name == ' ':
                            z=(filename.rstrip())
                            f=open(z+".txt",'w')
                            f.write(log)

                log1(str(N),str(filename),str(log))


                print('\n', "   ")
                
                if str(hour1) == "00" and  str(min1) == "00" and str(sec1) == "00":
                    if H != "0" and M !="0" and S !="0": # h m s 
                        a=str ("Your " + H +" hour " + M + " Minutes " +S + " Seconds " +N+ " Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
                    elif H != "0" and M =="0" and S =="0": # h
                        a=str ("Your " + H +" hour " +N+ " Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
                    elif H != "0" and M !="0" and S !="0": # h s 
                        a=str ("Your " + H +" hour " +S + " Seconds " +N+ " Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
                    elif H != "0" and M !="0" and S =="0": # h m
                        a=str ("Your " + H +" hour " +M+ "Minutes" +N+ " Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
                    elif H == "0" and M !="0" and S !="0": # m s
                        a=str ("Your "  + M + " Minutes " +S + " Seconds " +N+ " Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
                    elif H == "0" and M !="0" and S =="0": # m
                        a=str ("Your "  + M + " Minutes " + N+ " Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
                    elif H == "0" and M =="0" and S !="0": # s
                        a=str ("Your " + S + " Seconds"  +N+" Timer is complete")
                        print(a)
                        engine.say(a)
                        engine.runAndWait()
            min=min-1
            sec=60
        hour=hour-1
        min=59
  
    print('\n Timer Complete. \n')      

def len1():
    if "seconds" in g:
        if "name" in t:
            try:

                t1 = threading.Thread(name=g[-1],target=check, args=(0,0,int(res[0],),g[-1]), daemon = 'true')            
                t1.start()

                while t1.is_alive():
                    t1.join(1)
            
            except KeyboardInterrupt:           
                print("\n stopped \n")
        else:
            try:
                t1 = threading.Thread(target=check, args=(0,0,int(res[0],)), daemon = 'true')
                t1.start()

                while t1.is_alive():
                    t1.join(1)
            except KeyboardInterrupt:
                print("\n stopped \n")
            

    elif "hour" in g:
        if "name" in t:
            try:
                t2 = threading.Thread(target=check, args=(int(res[0]),0,0,g[-1]), daemon = 'true')
                t2.start()

                while t2.is_alive():
                    t2.join(1)

            except KeyboardInterrupt:           
                print("\n stopped \n") 
        else:
            try:
                t2 = threading.Thread(target=check, args=(int(res[0]),0,0,), daemon = 'true')
                t2.start()

                while t2.is_alive():
                    t2.join(1)

            except KeyboardInterrupt:           
                print("\n stopped \n")


    elif "minutes" in g:
        if "name" in t:
            try:
                t3 = threading.Thread(target=check, args=(0,int(res[0]),0,g[-1]), daemon = 'true')
                t3.start()

                while t3.is_alive():
                    t3.join(1)

            except KeyboardInterrupt:           
                print("\n stopped \n")
        else:
            try:
                t3 = threading.Thread(target=check, args=(0,int(res[0]),0,), daemon = 'true')
                t3.start()

                while t3.is_alive():
                    t3.join(1)

            except KeyboardInterrupt:           
                print("\n stopped \n")
            

def len2():

    if  "hour" in g:
        if "name" in t:
            try:
                t4 = threading.Thread(target=check, args=(int(res[0]),int(res[1]),0,g[-1]), daemon = 'true')
                t4.start()

                while t4.is_alive():
                    t4.join(1)
            
            except KeyboardInterrupt:        
                print("\n stopped \n")
        else:
            try:
                t4 = threading.Thread(target=check, args=(int(res[0]),int(res[1]),0,), daemon = 'true')
                t4.start()

                while t4.is_alive():
                    t4.join(1)
            
            except KeyboardInterrupt:        
                print("\n stopped \n")

            
          
    elif "minutes" in g:
        if "name" in t:
            try:
                t5 = threading.Thread(target=check, args=(0,int(res[0]),int(res[1],),g[-1]), daemon = 'true') 
                t5.start()

                while t5.is_alive():
                    t5.join(1)
            
            except KeyboardInterrupt:           
                print("\n stopped \n")
        else:
            try:
                t5 = threading.Thread(target=check, args=(0,int(res[0]),int(res[1],)), daemon = 'true') 
                t5.start()

                while t5.is_alive():
                    t5.join(1)
            
            except KeyboardInterrupt:           
                print("\n stopped \n")


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:    
        print("SET THE TIMER FUNCTION :")
        audio = r.listen(source)       
        try:
            text = r.recognize_google(audio)   
            t = str(text)
            #t=str("status about gym timer")
            print(t)
            print("You said : {}".format(text)) 
            res = [int(i) for i in t.split() if i.isdigit()] 
            res_len = len(res)         
            g = t.split()
            print(g[-1])

            if "status " in t:
                #print("status function working")
                k = ['what', 'is', "the",'status','timer','of','about'] 
                for i in k : 
                    t = t.replace(i, '') 
                #print ("Resultant list is : " + str(t)) 
                nlog=(t.strip())
                fname=nlog
                #print(fname)
                Lfile=open(fname+'.txt', 'r')
                data = Lfile.read().replace('\n', '')
                print(data)
                engine.say(data)
                engine.runAndWait()
            elif res_len == 1 :
               t13 = threading.Thread(target=len1, args=(), daemon = 'true') 
               t13.start()
            elif res_len == 2 :
               t14 = threading.Thread(target=len2, args=(), daemon = 'true') 
               t14.start()          
            elif t == "my timers" or "my timer":
                print("No of active timers :"+int(threading.active_count()/2))
          
        except:
            print("Sorry could not recognize your voice") 

            

      
      

       
