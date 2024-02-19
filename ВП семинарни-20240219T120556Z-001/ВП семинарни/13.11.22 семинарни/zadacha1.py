import datetime
import calendar
 
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])
 
# Driver program
date = "20 04 2005"
print(findDay(date))