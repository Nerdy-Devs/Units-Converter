from timefunctions import *

def convert_seconds_menu():
    choice = int(input("What do you want to convert seconds to?\n0:Minutes"))
    if choice == 0:
        secs = int(input("How many seconds would you like to convert? "))
        seconds, minutes = seconds_to_minutes(secs)
        print(str(secs) + " seconds is " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
def time_conversion_menu():
    choice=int(input("What type of time unit are you trying to convert?\n0:Seconds"))
    if choice == 0:
        convert_seconds_menu()
    else:
        print("Invalid time conversion")

def main():
    choice = int(input("What type of conversions would you like to do?\n0: Time\n"))
    if choice == 0:
        time_conversion_menu()
    else:
        print("Invalid conversion type")
main()