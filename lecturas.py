#!/usr/bin/env python3
import time
import subprocess
import threading

def funcion():
    p=subprocess.run(["python3","ignis.py","&"], stdout=subprocess.PIPE)

hilo=threading.Thread(target=funcion)

tegrastats_cmd = f"sudo tegrastats --interval 1000"
cmd = f"{{ echo $(date -u) & {tegrastats_cmd}; }} > datos_ignis.txt"
lecturas = subprocess.Popen(cmd, shell=True)

i=1

while True:
    
     if i==1:
        time.sleep(5)
        hilo.start()
        print("el algoritmo ya empezó")
     if i > 1 & hilo.is_alive() == False:
        print("ya terminó el algoritmo")
        time.sleep(5)
        lecturas.kill()
        break
     i=i+1
