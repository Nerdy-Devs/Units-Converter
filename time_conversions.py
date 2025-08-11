# !TODO! make these classes which have values (60000) and and also what there unit names (min) are
# and also "nice names" (minutes)

MILLISECONDS: int = 1
SECONDS: int = MILLISECONDS * 1000
MINUTES: int = SECONDS * 60
HOURS: int = MINUTES * 60
DAYS: int = HOURS * 24
WEEKS: int = DAYS * 7
YEARS: int = WEEKS * 52

values: list[int] = [MILLISECONDS, MINUTES, HOURS, DAYS, WEEKS, YEARS]