import time_conversions

def main():
    global verbose
    verbose = int(input("Would you like to activate verbose mode? (ex: 2 hours and 30 minutes)\n0:Yes\n1:No\n"))
    if verbose == 0 or verbose == 1:
        choice = int(input("What type of conversions would you like to do?\n0: Time\n"))
    else:
        print("Invalid setting")
    match choice:
        case 0:
            time_conversion_menu()
        case _:
            print("Invalid conversion type")

def unit_selector(siunit, type):
    if siunit -1 >= len(type.values) or siunit < 0:
        print("Invalid selection")
        return
    # Moves it one day for the array index
    siunit -= 1

def convert_seconds_menu():
    choice = int(input("What do you want to convert seconds to?\n1: Milliseconds\n2: Minutes\n3: Hours\n4: Days\n5: Weeks(non-leap)\n6: Years\n"))
    unit_selector(choice, time_conversions)

    # Get the seconds from the user
    seconds: float = float(input("How many seconds would you like to convert?: "))

    # If the choice isn't milliseconds, multiple the time by 1000
    # the conversion math uses milliseconds
    if choice != 5:
        seconds *= 1000
    
    # Calculates the converted time if verbose mode is off
    if verbose == 1:
        converted_time: float = seconds / time_conversions.values[choice]
        return print(converted_time)
    
    match choice:
        case 0:
            time_conversions.print_seconds_to_minutes(seconds)
        case 1:
            time_conversions.print_seconds_to_hours(seconds)
        case 2:
            time_conversions.print_seconds_to_days(seconds)
        case 3:
            time_conversions.print_seconds_to_weeks(seconds)
        case 4:
            time_conversions.print_seconds_to_months(seconds)
        case 5:
            time_conversions.print_seconds_to_years(seconds)
        case 6:
            time_conversions.print_seconds_to_milliseconds(seconds)
        case _:
            print("Invalid seconds conversion")
    
def time_conversion_menu():
    choice=int(input("What type of time unit are you trying to convert?\n0: Seconds\n"))
    match choice:
        case 0:
            convert_seconds_menu()
        case _:
            print("Invalid time conversion")

main()

# Test
#def intput(question: str):
#    return int(input(question))