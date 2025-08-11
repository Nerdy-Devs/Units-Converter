def seconds_to_minutes(secs):
    minutes = secs // 60
    seconds = secs % 60
    return minutes, seconds
def print_seconds_to_minutes(secs):
    minutes, seconds = seconds_to_minutes(secs)
    print(f"{secs} seconds is {minutes} minutes, and {seconds} seconds.")
def seconds_to_hours(secs):
    hours = secs // 3600
    minutes, seconds = seconds_to_minutes(secs % 3600)
    return hours, minutes, seconds
def print_seconds_to_hours(secs):
    hours, minutes, seconds = seconds_to_hours(secs)
    print(f"{secs} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")
def seconds_to_days(secs):
    days = secs // 86400
    hours, minutes, seconds = seconds_to_hours(secs % 86400)
    return days, hours, minutes, seconds
def print_seconds_to_days(secs):
    days, hours, minutes, seconds = seconds_to_days(secs)
    print(f"{secs} seconds is {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")
def seconds_to_weeks(secs):
    weeks = secs // 604800
    days, hours, minutes, seconds = seconds_to_days(secs % 604800)
    return weeks, days, hours, minutes, seconds
def print_seconds_to_weeks(secs):
    weeks, days, hours, minutes, seconds = seconds_to_weeks(secs)
    print(f"{secs} seconds is {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_months(secs):
    months = secs // 2592000
    weeks, days, hours, minutes, seconds = seconds_to_days(secs % 2592000)
    return months, weeks, days, hours, minutes, seconds

def print_seconds_to_months(secs):
    months, weeks, days, hours, minutes, seconds = seconds_to_months(secs)
    print(f"{secs} seconds is {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_years(secs):
    years = secs // 31556952
    months, weeks, days, hours, minutes, seconds = seconds_to_months(secs % 31556952)
    return years, months, weeks, days, hours, minutes, seconds

def print_seconds_to_years(secs):
    years, months, weeks, days, hours, minutes, seconds = seconds_to_years(secs)
    print(f"{secs} seconds is {years} years, {months} months, {weeks} weeks, {days} days, {hours} hours, {minutes} minutes, and {seconds} seconds.")

def seconds_to_milliseconds(secs):
    milliseconds = secs * 1000
    return milliseconds
def print_seconds_to_milliseconds(secs):
    milliseconds = seconds_to_milliseconds
    print(f"{milliseconds/1000} seconds is {milliseconds} milliseconds.")