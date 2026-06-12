#!/usr/bin/env python3

'''
OPS445 Assignment 1
Program: assignment1.py 
Author: "Student Name"
Semester: "Fall/Winter/Summer YYYY"

The python code in this file (assignment1.py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]


def mon_max(month:int, year:int) -> int:
    #returns the maximum day for a given month. Includes leap year check


    #Return the maximum number of days in the given month.

    if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28

    month_days = {
        1:31, 3:31, 4:30,
        5:31, 6:30, 7:31, 8:31,
        9:30, 10:31, 11:30, 12:31
    }

    return month_days[month]

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    
    

    

    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date


def usage():
    "Print a usage message to the user"
    ...


def leap_year(year: int) -> bool:
    "return True if the year is a leap year"
   
    #Return True if year is a leap year, otherwise False.

    if year % 400 == 0:
        return True

    elif year % 100 == 0:
        return False

    elif year % 4 == 0:
        return True
    else:
        return False

def valid_date(date: str) -> bool:
    "check validity of date and return True if valid"
    try:
        year, month, day = date.split("-")
        if len(year)!=4 or len(month)!=2 or len(day)!=2:
            return False


        year = int(year)
        month = int(month)
        day = int(day)

        if month < 1 or month > 12:
            return False
        

        if day < 1 or day > mon_max(month, year):
            return False
        return True
    except:
        return False

def day_count(start_date: str, stop_date: str) -> int:
    "Loops through range of dates, and returns number of weekend days"
#keep track of number of weekend days found
    weekend_count = 0

#start checking from the first date in the range
    current_date = start_date
#Continue until all dates in the range have been checked 
    while True:
        year_str, month_str, day_str = current_date.split("-")
        year=int(year_str)
        month=int(month_str)
        day=int(day_str)
        weekday = day_of_week(year, month, day)
#Add a count after every weekday
        if weekday == "sat" or weekday == "sun":
            weekend_count +=1
#Stop at end date
        if current_date == stop_date:
            break
        current_date=after(current_date)
#return the total number or weekend days found
    return weekend_count

#check Script
if __name__ == "__main__":
    print(after("2025-02-26"))
    print(after("2024-02-28"))
    print(after("2025-02-28"))
    print(after("2023-12-31"))
    print(valid_date("2024-03-29"))
    print(day_count("2024-01-29", "2024-03-29"))
