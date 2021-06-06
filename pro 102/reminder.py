import time

start= time.time()
#reminderObj = [str(r) for r in input("Enter the things you want to be reminded:").split(', ')]
#print("\n",r)
reminderObj=input("Enter the things you want to be reminded seprated by a comma:").split(',')
time_to_repete=input("Enter the time you want the timer to repeat:")

reminderList = []
for r in reminderObj:
    remind=r
    reminderList.append(remind)

if ((time.time()-start)>=3600):
    print("the things you need to do are:",*reminderList,sep = "\n")
    reminderObj=input("If you have to change the reminder then type here:").split(",")
    time_to_repete=input("Enter the time you want the timer to repeat:")