import os
import re
import shutil

def removezero(rootpath):
    pths = []
    ext = [".pdf"]
    for subdirs, dirs, files in os.walk(rootpath):
        for filename in files:
            if filename.lower().endswith(tuple(ext)):
                pths.append(os.path.join(subdirs,filename))
                
    for i in pths:
        print(str(i))	
        try:
            with open(str(i), "rb") as f:
                f1=re.search(b'\x25\x50\x44\x46', f.read(100))
                f.seek(0)
                f2=re.search(b'\x3C', f.read(10))
                f.seek(0)
                #f13=re.search(b'\x25\x50\x44\x46\x2D\x31\x2E\x37', f.read(100))
                #f.seek(0)
                
                #print ("moved")
                if ((f1 is None) and (f2 is None)):
                        try:
                            print ("bad file found")
                            f.close()
                            shutil.move(str(i), "./bad")
                            print(str(i) + " moved")
                        except:
                            continue
        except:
            continue

rootpath = input("Escreva o caminho da pasta raiz: ")
c=0
while True:               
    os.mkdir("./bad")
    try:
        removezero(rootpath)
    except:
        continue
    os.rename('./bad', './bad_' + str(c))
    c+=1
    if c == 30:
        c = 0
        input('Enter...')
