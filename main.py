from timefunctions import *

def convert_seconds_menu():
    choice = int(input("What do you want to convert seconds to?\n0:Minutes\n1:Hours\n2:Days"))
    secs = int(input("How many seconds would you like to convert? "))
    if choice == 0:
        seconds, minutes = seconds_to_minutes(secs)
        print(str(secs) + " seconds is " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
    elif choice == 1:
        seconds, minutes, hours = seconds_to_hours(secs)
        print(str(secs) + " seconds is " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
    elif choice == 2:
        seconds, minutes, hours, days = seconds_to_days(secs)
        print(str(secs) + " seconds is " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
    else:
        print("Invalid seconds conversion")
def time_conversion_menu():
    choice=int(input("What type of time unit are you trying to convert?\n0:Seconds\n"))
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