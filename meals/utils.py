from datetime import date, timedelta, datetime
import time
import calendar

def get_date():
    today_date = date.today()
    date_arr = []
    monday_date = today_date - timedelta(today_date.weekday())
    for i in range (0,6):
        date_arr.append(monday_date + timedelta(i))
    return date_arr
    
def convert_list_dict():
    date_arr = get_date()
    return {calendar.day_abbr[key]: value for key, value in enumerate(date_arr)}

def get_current_time():
    my_time = time.strftime('%H')
    return int(my_time)

