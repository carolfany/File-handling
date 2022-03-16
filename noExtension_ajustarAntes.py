import os
import re
import shutil

def removezero(rootpath):
    pths = []
    ext = [""] #TROCAR AQUI PARA BUSCAR EM TODAS AS EXTENSÕES OU EM UMA EM ESPECÍFICO
    for subdirs, dirs, files in os.walk(rootpath):
        for filename in files:
            if filename.lower().endswith(tuple(ext)):
                pths.append(os.path.join(subdirs,filename))
                
    for i in pths:
        print(str(i))	
        try:
            with open(str(i), "rb") as f:
                if (re.search(b'\xEF\xBB\xBF\x3C', f.read(100))): #TROCAR AQUI O HEADER QUE DESEJA BUSCAR (por exemplo pdf, doc, mp3, zip, etc.
                    try:
                        print ("File found.")
                        f.close()
                        os.rename(str(i), str(i) + '.extensãoBuscada') #TROCAR AQUI O "extensãoBuscada" PELA EXTENSÃO CONFORME HEADER QUE ESTÁ BUSCANDO
                        print ("File renamed.")
                    except:
                        continue
        except:
            continue

rootpath = input("Escreva o caminho da pasta raiz: ")
c=0
while c<1:               
    try:
        removezero(rootpath)
    except:
        continue
    c+=1
    print("Session Done")
