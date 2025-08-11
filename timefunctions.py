import math

def seconds_to_minutes(secs):
    minutes = math.floor(secs / 60)
    seconds = secs % 60
    return minutes, seconds