# https://www.hackerrank.com/challenges/time-conversion/problem
from datetime import datetime

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    timeObj = datetime.strptime(s, '%I:%M:%S%p')

    return timeObj.strftime("%H:%M:%S")

input = '07:05:45PM'

print timeConversion(input)