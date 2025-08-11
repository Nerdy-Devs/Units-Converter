import math

def seconds_to_minutes(secs):
    minutes = math.floor(secs / 60)
    seconds = secs % 60
    return minutes, seconds
def seconds_to_hours(secs):
    hours = math.floor(secs / 3600)
    minutes, seconds = seconds_to_minutes(secs % 3600)
    return hours, minutes, seconds
def seconds_to_days(secs):
    days = math.floor(secs / 86400)
    hours, minutes, seconds = seconds_to_hours(secs % 86400)
    return days, hours, minutes, seconds