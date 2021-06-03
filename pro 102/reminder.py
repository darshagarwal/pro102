import time

start= time.time()
#reminderObj = [str(r) for r in input("Enter the things you want to be reminded:").split(', ')]
#print("\n",r)
reminderObj=input("Enter the things you want to be reminded seprated by a comma:").split(', ')

for r in reminderObj:
    remind=r

if ((time.time()-start)>=2):
    print("the things you need to do are:",remind)
    reminderObj=input("If you have to change the reminder then type here:").split(",")