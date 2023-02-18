"""
1. Write a Python program to display the current date and time.

Expected output:
The current date and time, in the format "Month Day, Year Hours: Minutes: Seconds."

"""
# Solution 1

# import datetime

# print(datetime.datetime.now())

"""
Challenge: Append the text st, nd, rd, and th to end of the days.

Notes:

1st <-- Pattern?
2nd <-- 
3rd <--
4th <--
5th <-- Pattern?
6th
7th
8th
... etc.

Somehow, I need to write a control flow statement that describes this:

- If the date (day) ends in a 1, 2, or 3, then append "st", "nd", "rd", respectively.

- But, if the the date ends in a 4, 5, 6, 7, 8, or 9, then append "th".

- I also realized that I probably need to access the specific index of the number too if I want to add the ending next to it. Otherwise, the endings might get added to the front and I'll end up with something like this: "1st2nd".
"""

# Solution 2 - My Solution

import datetime

current = datetime.datetime.now()
current_year = current.year
current_month = current.month
current_day = current.day

months = [
    current,
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

month = months[current_month]
day = current_day
year = current_year


def format_current_date():

    if current_day % 10 == 1:
        day = str(current_day) + "st"

    elif current_day % 10 == 2:
        day = str(current_day) + "nd"

    elif current_day % 10 == 3:
        day = str(current_day) + "rd"

    elif current_day % 10 == 4:
        day = str(current_day) + "rd"

    else:
        day = str(current_day) + "th"

    return print(f"Today is {day} of {month}, {year}")


print(format_current_date())

"""
What I learned from how I could have improved this solution:

- In the format_current_date function, I learned that I didn't need to pass in month and day as arguments since they are already global variables defined at the top of the script.

- Instead of hardcoding the months list, I could have used the calendar module to get the month name from the month number. For example, I could replace the line month = months[current_month] with month = calendar.month_name[current_month].

- When appending the suffix to the day, I should've converted the integer current_day to a string before concatenating it with the suffix, so that you don't get a type error.

- In the control flow statements that add the suffix to the day, I had a typo: I had "nd" twice for the suffix for numbers ending in 2 or 3.

- Instead of printing the formatted date in the format_current_date function, I could have returned the formatted string and then print it outside of the function.

- I could have added some error handling to my code to handle cases where the current day or month is not in the expected range.

"""

# # Refactored Solution:

# import datetime

# current = datetime.datetime.now()
# current_year = current.year
# current_month = current.strftime("%B")  # get the month name in string format
# current_day = current.day
# year = current_year


# def format_current_date(day, month, year):
#     if day % 10 == 1 and day != 11:
#         suffix = "st"
#     elif day % 10 == 2 and day != 12:
#         suffix = "nd"
#     elif day % 10 == 3 and day != 13:
#         suffix = "rd"
#     else:
#         suffix = "th"

#     print(f"Today is the {day}{suffix} of {month}, {year}")


# format_current_date(current_day, current_month, year)

