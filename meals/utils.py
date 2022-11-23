from datetime import date, timedelta
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

