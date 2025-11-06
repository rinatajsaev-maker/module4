#Author:Rinat.R
#Date:10.18.25
"""this program calculates the time after a given number of hours"""
currentTimeStr = input("What is the current time (in hours 0-23)?")
waitTimeStr = input("How many hours do you want to wait")

currentTimeInt = int(currentTimeStr)
waitTimeInt = int(waitTimestr)

finalTimeInt = currentTimeInt + waitTimeInt
print(finalTimeInt)

