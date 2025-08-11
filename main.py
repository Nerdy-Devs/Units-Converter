from timefunctions import *

def convert_seconds_menu():
    choice = int(input("What do you want to convert seconds to?\n0:Minutes\n1:Hours\n2:Days\n3:Weeks\n4:Months (30 days long)"))
    secs = int(input("How many seconds would you like to convert?: "))
    match choice:
        case 0:
            seconds_to_minutes(secs)
        case 1:
            seconds_to_hours(secs)
        case 2:
            seconds_to_days(secs)
        case 3:
            seconds_to_weeks(secs)
        case 4:
            seconds_to_months(secs)
        case _:
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