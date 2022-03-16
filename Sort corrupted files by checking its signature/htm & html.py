import os
import re
import shutil

def removezero(rootpath):
    pths = []
    ext = [".htm", ".html", ".HTM", ".HTML"]
    for subdirs, dirs, files in os.walk(rootpath):
        for filename in files:
            if filename.lower().endswith(tuple(ext)):
                pths.append(os.path.join(subdirs,filename))
                
    for i in pths:
        print(str(i))	
        try:
            with open(str(i), "rb") as f:
                f1=re.search(b'\x3C', f.read(10))
                f.seek(0)

                f7=re.search(b'\xFF\xFE\x3C\x00', f.read(100))
                f.seek(0)

                f8=re.search(b'\x0A\x3C\x21\x2D', f.read(100))
                f.seek(0)

                f9=re.search(b'\x46\x72\x6F\x6D', f.read(100))
                f.seek(0)
                
                #print ("searching")
                if ((f1 is None) and (f7 is None) and (f8 is None) and (f9 is None)):
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
    if(c == 30):
        c = 0
        input('Enter...')
