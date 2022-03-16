import os
import re
import shutil

def removezero(rootpath):
    pths = []
    ext = [""] #swap this part to seek in all file extensions ([""]) or in a particular one (such as: [".pdf"])
    for subdirs, dirs, files in os.walk(rootpath):
        for filename in files:
            if filename.lower().endswith(tuple(ext)):
                pths.append(os.path.join(subdirs,filename))
                
    for i in pths:
        print(str(i))	
        try:
            with open(str(i), "rb") as f:
                if (re.search(b'\xEF\xBB\xBF\x3C', f.read(100))): #Change here the file signature you need to look for (such as pdf, doc, mp3, zip...)
                    try:
                        print ("File found.")
                        f.close()
                        os.rename(str(i), str(i) + '.extension') #Change "extension" for the actual extension of the file signature searched for above
                        print ("File renamed.")
                    except:
                        continue
        except:
            continue

rootpath = input("Paste here the root directory you want to search on: ")
c=0
while c<1:               
    try:
        removezero(rootpath)
    except:
        continue
    c+=1
    print("Session Done")
