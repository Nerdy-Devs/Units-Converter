def seconds_to_minutes(secs: int):
    return secs / 60, secs

def print_seconds_to_minutes(secs: int):
    minutes, seconds = seconds_to_minutes(secs)
    print(f"{secs} seconds is {minutes} minutes, and {seconds} seconds.")

def seconds_to_hours(secs: int):
    hours = secs // 3600
    minutes, seconds = seconds_to_minutes(secs % 3600)
    return hours, minutes, seconds

def print_seconds_to_hours(secs: int):
    hours, minutes, seconds = seconds_to_hours(secs)
    print(f"{secs} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_days(secs: int):
    days = secs // 86400
    hours, minutes, seconds = seconds_to_hours(secs % 86400)
    return days, hours, minutes, seconds

def print_seconds_to_days(secs: int):
    days, hours, minutes, seconds = seconds_to_days(secs)
    print(f"{secs} seconds is {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_weeks(secs: int):
    weeks = secs // 604800
    days, hours, minutes, seconds = seconds_to_days(secs % 604800)
    return weeks, days, hours, minutes, seconds

def print_seconds_to_weeks(secs: int):
    weeks, days, hours, minutes, seconds = seconds_to_weeks(secs)
    print(f"{secs} seconds is {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_months(secs: int):
    months = secs // 2592000
    weeks, days, hours, minutes, seconds = seconds_to_weeks(secs % 2592000)
    return months, weeks, days, hours, minutes, seconds

def print_seconds_to_months(secs: int):
    months, weeks, days, hours, minutes, seconds = seconds_to_months(secs)
    print(f"{secs} seconds is {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_years(secs: int):
    years = secs // 31556952
    months, weeks, days, hours, minutes, seconds = seconds_to_months(secs % 31556952)
    return years, months, weeks, days, hours, minutes, seconds

def print_seconds_to_years(secs: int):
    years, months, weeks, days, hours, minutes, seconds = seconds_to_years(secs)
    print(f"{secs} seconds is {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_milliseconds(secs: int):
    milliseconds = secs * 1000
    return milliseconds

def print_seconds_to_milliseconds(secs: int):
    print(f"{secs} seconds is {secs * 1000} milliseconds.")