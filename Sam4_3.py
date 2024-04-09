import datetime
import time

counter = 5
while counter > 0:
    print(datetime.datetime.now())
    time.sleep(1)
    counter = counter - 1

