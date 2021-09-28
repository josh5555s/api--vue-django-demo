from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta
import calendar
import time

todays_date = date.today() 
# todays_date = datetime(2021, 9, 26) # try dates other than today to test
weekend_is_passed = False
next_month_date = todays_date.replace(day=1) + relativedelta(months=1)

def create_weekend_dates(reoccuring_weekend):
    if reoccuring_weekend == 'Last Weekend':
        def find_next_last_weekend(date):
            today_dom = date.day
            _ , days_in_month = calendar.monthrange(date.year, date.month)
            last_doms_dow = datetime(date.year, date.month, days_in_month).weekday()
            last_sunday = days_in_month
            if last_doms_dow != 6:
                last_sunday = days_in_month - (last_doms_dow + 1)
            last_friday = last_sunday - 2
            if today_dom > last_sunday:
                global weekend_is_passed
                weekend_is_passed = True

            friday_date = datetime(date.year, date.month, last_friday, 1)
            sunday_date = datetime(date.year, date.month, last_sunday, 23)
            return friday_date, sunday_date 

        friday_date, sunday_date = find_next_last_weekend(todays_date)
        if weekend_is_passed:
            friday_date, sunday_date = find_next_last_weekend(next_month_date)

        # add epoch time for conversion to js date object
        friday_date_time = time.mktime(friday_date.timetuple())
        sunday_date_time = time.mktime(sunday_date.timetuple())
        return friday_date, friday_date_time, sunday_date, sunday_date_time

    else:
        def find_other_weekends(date, reoccuring_weekend):
            today_dom = date.day
            extra_week = 0
            if reoccuring_weekend == '2nd Weekend':
                extra_week = 7
            elif reoccuring_weekend == '3rd Weekend':
                extra_week = 14
            
            first_doms_dow, _ = calendar.monthrange(date.year, date.month)
            days_until_first_friday = 4 - first_doms_dow
            first_friday_dom = days_until_first_friday + 1
            friday_dom = first_friday_dom + extra_week
            if today_dom > friday_dom:
                global weekend_is_passed
                weekend_is_passed = True

            friday_date = datetime(date.year, date.month, friday_dom, 1)
            sunday_date = datetime(date.year, date.month, friday_dom + 2, 23)
            return friday_date, sunday_date 

        friday_date, sunday_date = find_other_weekends(todays_date, reoccuring_weekend)
        if weekend_is_passed:
            friday_date, sunday_date = find_other_weekends(next_month_date, reoccuring_weekend)

        # add epoch time for conversion to js date object
        friday_date_time = time.mktime(friday_date.timetuple())
        sunday_date_time = time.mktime(sunday_date.timetuple())
        print(friday_date_time)
        print(type(friday_date_time))
        return friday_date, friday_date_time, sunday_date, sunday_date_time
                
