import time

start= time.time()
#reminderObj = [str(r) for r in input("Enter the things you want to be reminded:").split(', ')]
#print("\n",r)
reminderObj=input("Enter the things you want to be reminded seprated by a comma:").split(',')

reminderList = []
for r in reminderObj:
    remind=r
    reminderList.append(remind)

if ((time.time()-start)>=2):
    print("the things you need to do are:",reminderList)
    reminderObj=input("If you have to change the reminder then type here:").split(",")
