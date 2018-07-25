import datetime
import os
import io

print("Which day is this when you are running the script")
print("Enter it in following format\n")
print("If it is Sunday    : Enter 0")
print("If it is Monday    : Enter 1")
print("If it is Tuesday   : Enter 2")
print("If it is Wednesday : Enter 3")
print("If it is Thursday  : Enter 4")
print("If it is Friday    : Enter 5")
print("If it is Saturday  : Enter 6")
day=input("Enter The Appropriate Number :")
print("Paste here the complete path to the vpn.py file")
path=raw_input()
t=datetime.datetime.time(datetime.datetime.now())
hr=int(t.hour)+1
minute=int(t.minute)+35
minute=minute%60
hr=hr%24
log=str(minute)+" "+str(hr)+" "+"*"+" "+"*"+" "+str(day)+" "+"python"+" "+path

hr2=(hr+3)%24

log2=str(minute)+" "+str(hr2)+" "+"*"+" "+"*"+" "+str(day)+" "+"python"+" "+path

hr3=(hr+7)%24
log3=str(minute)+" "+str(hr3)+" "+"*"+" "+"*"+" "+str(day)+" "+"python"+" "+path

hr4=(hr+12)%24
log4=str(minute)+" "+str(hr4)+" "+"*"+" "+"*"+" "+str(day)+" "+"python"+" "+path

os.system("python"+" "+"vpn.py")

f=open("cron_list.txt","w+")
f.write(log+"\n")
f.write(log2+"\n")
f.write(log3+"\n")
f.write(log4)

f.seek(0,2)

f.close()
os.system("chmod +x vpn.py")
os.system("sudo ln -s path /etc/cron.daily/vpn")
