def seconds_to_minutes(secs):
    minutes = secs // 60
    seconds = secs % 60
    print(str(secs) + " seconds is " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
    return minutes, seconds
def seconds_to_hours(secs):
    hours = secs // 3600
    minutes, seconds = seconds_to_minutes(secs % 3600)
    print(str(secs) + " seconds is " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
    return hours, minutes, seconds
def seconds_to_days(secs):
    days = secs // 86400
    hours, minutes, seconds = seconds_to_hours(secs % 86400)
    print(str(secs) + " seconds is " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
    return days, hours, minutes, seconds
def seconds_to_weeks(secs):
    weeks = secs // 604800
    days, hours, minutes, seconds = seconds_to_days(secs % 604800)
    print(str(secs) + " seconds is " + str(weeks) + " weeks, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
    return weeks, days, hours, minutes, seconds
def seconds_to_months(secs):
    months = secs // 2592000
    weeks, days, hours, minutes, seconds = seconds_to_days(secs % 2592000)
    print(str(secs) + " seconds is " + str(months) + " weeks, " + str(weeks) + " weeks, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")
    return months, weeks, days, hours, minutes, seconds

# Test cases go here. You have no idea how easy it is to fuck up simple math.
# Love, James <3

if __name__ == "__main__":
    test = int(input("Which test do you have the displeasure of running?\n0:Seconds\n"))
    match test:
        case 0:
            print(seconds_to_minutes(60))
            print(seconds_to_minutes(81)) # Should return 1m21s
            print(seconds_to_minutes(96)) # Should return 1m36s
            print(seconds_to_hours(3600))
            print(seconds_to_hours(953)) # Should return 0h15m53s
            print(seconds_to_hours(7232)) # Should return 2h0m32s
            print(seconds_to_days(86400))
            print(seconds_to_days(9073)) # Should return 0d2h31m13s
            print(seconds_to_days(57993)) # Should return 0d16h6m33s
            print(seconds_to_weeks(604800))
            print(seconds_to_weeks(970893)) # Should return 1w4d5h41m33s
            print(seconds_to_weeks(95498)) # Should return 0w1d2h31m38s
            # TODO: Add test cases for seconds -> months
            # print(seconds_to_months(2592000))
            # print(seconds_to_months(2592000))
            # print(seconds_to_months(2592000))
        case _:
            print("Wrong test dumbass")