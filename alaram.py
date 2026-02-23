import time
import datetime
alaram_time=input("enter alaram time(HH:MM:SS-24 hour format)")
while True:
    current_time=datetime.datetime.now().strftime('%H:%M:%S')
    if alaram_time!=current_time:
        print("it s not")
    else:
        print("it is awaken time")
        break
    time.sleep(1)
