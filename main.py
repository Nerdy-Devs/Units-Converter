from timefunctions import *
from time_conversions import time_milliseconds 


def convert_seconds_menu():
    choice = int(input("What do you want to convert seconds to?\n1: Milliseconds\n2: Minutes\n3: Hours\n4: Days\n5: Weeks(non-leap)\n6: Years\n"))

    if choice -1 >= len(time_milliseconds.values) or choice < 0:
        print("Invalid selection")
        return

    # Moves it one day for the array index
    choice -= 1

    # Get the seconds from the user
    seconds: float = float(input("How many seconds would you like to convert?: "))

    # If the choice isn't milliseconds, multiple the time by 1000
    # the conversion math uses milliseconds
    if choice != 5:
        seconds *= 1000
    
    # Calculates the converted time
    converted_time: float = seconds / time_milliseconds.values[choice]

    print(converted_time)
    
def time_conversion_menu():
    choice=int(input("What type of time unit are you trying to convert?\n0: Seconds\n"))
    match choice:
        case 0:
            convert_seconds_menu()
        case _:
            print("Invalid time conversion")

def main():
    choice = int(input("What type of conversions would you like to do?\n0: Time\n"))
    match choice:
        case 0:
            time_conversion_menu()
        case _:
            print("Invalid conversion type")
main()

# Test
def intput(question: str):
    return int(input(question))