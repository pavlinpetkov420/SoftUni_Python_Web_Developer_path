centuries = int(input())
years = centuries * 100
days = int(years * 365.2422)
hours = days * 24
minutes = hours * 60
output = "{} centuries = {} years = {} days = {} hours = {} minutes"\
    .format(centuries, years, days, hours, minutes)
print(output)
