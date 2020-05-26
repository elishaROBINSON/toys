import time
import os

p=os.popen("ls").readlines()


for i in p:
	a=i.replace("\n","")
	os.system("zip -r -fz -f "+"zcompressed/"+a+".zip"+" "+a+" -x zcompressed")