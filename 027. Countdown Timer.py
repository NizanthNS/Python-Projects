# Countdown Timer Program

import time

while True:
    try:
        my_time = int(input("Enter the Time in Seconds: "))
        break
    except ValueError:
        print("Please Enter a valid Input")

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02} : {minutes:02} : {seconds:02}")
    time.sleep(1)

print("Time's Up!")