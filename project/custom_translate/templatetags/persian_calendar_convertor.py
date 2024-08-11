from jdatetime import datetime as jdatetime_datetime
from django import template
# from django_jalali.templatetags import jformat
from pytz import timezone
from datetime import datetime

register = template.Library()

# Convert the given Gregorian datetime to Persian calendar
@register.filter
def convert_to_persian_calendar(gregorian_datetime):
    utc_timezone = timezone('UTC')
    tehran_timezone = timezone('Asia/Tehran')
    tehran_datetime = gregorian_datetime.astimezone(tehran_timezone)

    persian_datetime = jdatetime_datetime.fromgregorian(datetime=tehran_datetime, tz=tehran_timezone, locale='fa_IR')
    return persian_datetime

# Convert the given Persian datetime to a formatted string
@register.filter
def format_persian_datetime(persian_datetime):
    persian_month_names = {
        1: 'فروردین', 
        2: 'اردیبهشت', 
        3: 'خرداد',
        4: 'تیر', 
        5: 'مرداد', 
        6: 'شهریور',
        7: 'مهر', 
        8: 'آبان', 
        9: 'آذر',
        10: 'دی', 
        11: 'بهمن', 
        12: 'اسفند'
    }
    persian_day_names = [ 
        'سه‌شنبه',
        'چهارشنبه', 
        'پنج‌شنبه', 
        'جمعه', 
        'شنبه',
        'یکشنبه',
        'دوشنبه',
    ]

    persian_day = persian_datetime.day
    persian_month = persian_month_names[persian_datetime.month]
    persian_year = persian_datetime.year
    persian_hour = persian_datetime.hour
    persian_minute = persian_datetime.minute
    persian_weekday = datetime(persian_datetime.year,persian_datetime.month,persian_datetime.day).weekday()

    return f"{persian_day_names[persian_weekday]} {persian_day} {persian_month} {persian_year}، ساعت {persian_hour}:{persian_minute:02d}"