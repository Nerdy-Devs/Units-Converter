from timefunctions import *

converter = int(input("What type of conversions would you like to do?\n0: Time\n"))

if converter == 0:
    timeconverter=int(input("What type of time conversion would you like to do?\n0:Seconds to Minutes"))
    if timeconverter == 0:
        secs = int(input("How many seconds would you like to convert? "))
        seconds, minutes = seconds_to_minutes(secs)
        print(str(secs) + " seconds is " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
    else:
        print("Invalid time conversion")
else:
    print("Invalid type of conversion")