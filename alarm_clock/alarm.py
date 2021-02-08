import datetime
import winsound
from colors import Colors
import time
# Coloring the console if necessary
color = Colors()
# function to take input in the form of hour and minute
def get_clock():
    global dt
    print(f"\n{color.BOLD}You will enter a time when you want to be waken...\n{color.ENDC}")
    time.sleep(1)
    dt = input(f"{color.OKGREEN}Enter the time ({color.BOLD}00:00 - 12:00): {color.ENDC}")
# counting down
def count_down(alarm):
    today = datetime.datetime.now()
    today_ = today.strftime("%H:%M")
    
    
    while(today_ != alarm):
        time_ = today.strftime("%H:%M:%S")
        
        print(f"{color.OKGREEN}{time_}{color.ENDC}")
        print()
        time.sleep(1)
        
        today = datetime.datetime.now()
        today_ = today.strftime("%H:%M")
    #Playing sound
    try:

        winsound.Beep(7700,10000)

    except RuntimeError:

        print(f"{color.WARNING}UNABLE TO PLAY SOUND{color.ENDC}")

# Run program
while True:
    entry = input(f"{color.OKGREEN}\nDo you want to set an alarm?--(yes/no) -- > {color.ENDC}")
    if entry.lower() == "yes":
        get_clock()

        print(f"{color.OKGREEN}\nYour alarm is being set...{color.ENDC}\n")
        time.sleep(0.7)
        print(f"{color.BOLD}Processing...{color.ENDC}\n")
        time.sleep(0.6)
        print(f"{color.BOLD}Countdown is starting...{color.ENDC}\n")
        time.sleep(0.5)

        count_down(dt)

        
    else:
        print(f"{color.BOLD}Exited!!{color.ENDC}")
        break



