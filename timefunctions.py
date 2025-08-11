import math

def seconds_to_minutes(secs):
    minutes = math.floor(secs / 60)
    seconds = secs % 60
    return minutes, seconds
def seconds_to_hours(secs):
    hours = math.floor(secs / 3600)
    minutes, seconds = seconds_to_minutes(secs % 3600)
    return hours, minutes, seconds