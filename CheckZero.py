import os
import re
import shutil

def removezero(rootpath, ext):
    pths = []      

    
    for subdirs, dirs, files in os.walk(rootpath):
        for filename in files:
            #if filename.lower().endswith(ext):
            if filename.lower():
                pths.append(os.path.join(subdirs,filename))
                
    for i in pths:
    
        zeroByte = 0
        
        print(str(i))	
        
        try:
            with open(str(i), "rb") as f:
            
                totalSize = os.path.getsize( str(i) )

                blob_data = bytearray(f.read())
                
                for byte in blob_data:
                
                    if byte == 0:
                    
                        zeroByte += 1

  
                if zeroByte == totalSize:
                
                    print("empety file")
                    f.close()
                    shutil.move(str(i), "./bad")
                    print(str(i) + " moved")

        except:
            continue

rootpath = input("Escreva o caminho da pasta raiz: ")
#ext = '.' + input('Escolha a extensão: ')
ext = [" "]
c=0

print(ext)
while True:               
    os.mkdir("./bad")
    try:
        removezero(rootpath, ext)
    except:
        continue
    os.rename('./bad', './bad_' + str(c))
    c+=1
    if c == 10:
        c = 0
        input('Enter...')
