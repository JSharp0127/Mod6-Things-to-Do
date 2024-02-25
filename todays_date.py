"""Chapter 13 Things to do"""
from datetime import date
today_string = ''
with open('today.txt') as f:
    month= int(f.read(1))
    day= int(f.read(3))
    year= int(f.read())
   
date = date(year, month, day)
fmt = "It's %A, %B %d, %Y"
print(date.strftime(fmt))
