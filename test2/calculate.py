"""
def readable_timedelta(days):
    week=days//7
    days_out = days% 7
    print(f"{week} weeks {days_out} days")

readable_timedelta(6)


egg_count = 0

def buy_eggs():
    egg_count += 12 # purchase a dozen eggs

buy_eggs()

str1 = 'Functions are important programming concepts.'

def print_fn():
    str1 = 'Variable scope is an important concept.'
    print(str1)

print_fn()
"""

def readable_timedelta(days):

    """Returns the days in a readable format as weeks and days"""
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)