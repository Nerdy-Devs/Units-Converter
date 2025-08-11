def seconds_to_minutes(secs):
    minutes = secs // 60
    seconds = secs % 60
    print(str(secs) + " seconds is " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
def seconds_to_hours(secs):
    hours = secs // 3600
    minutes, seconds = seconds_to_minutes(secs % 3600)
    print(str(secs) + " seconds is " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
def seconds_to_days(secs):
    days = secs // 86400
    hours, minutes, seconds = seconds_to_hours(secs % 86400)
    print(str(secs) + " seconds is " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")
def seconds_to_weeks(secs):
    weeks = secs // 604800
    days, hours, minutes, seconds = seconds_to_days(secs % 604800)
    print(str(secs) + " seconds is " + str(weeks) + " weeks, " + str(days) + " days, " + str(hours) + " hours, " + str(minutes) + " minutes and " + str(seconds) + " seconds.")