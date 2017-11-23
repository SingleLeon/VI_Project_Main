import time


def utc_mktime(DATE, TIME):
    """Returns number of seconds elapsed since epoch
 
    Note that no timezone are taken into consideration.
 
    utc tuple must be: (year, month, day, hour, minute, second)
    """
    if 170101 < DATE < 180101:  # 年月日
        utc_tuple = (int(DATE / 10000) + 2000,
                     int((DATE - int(DATE / 10000) * 10000) / 100),
                     int(DATE - int(DATE / 100) * 100),
                     int(TIME / 10000),
                     int((TIME - int(TIME / 10000) * 10000) / 100),
                     int(TIME - int(TIME / 100) * 100),
                     0, 0, 0)
    else:   # 日月年
        utc_tuple = (int(DATE - int(DATE / 100) * 100) + 2000,
                     int((DATE - int(DATE / 10000) * 10000) / 100),
                     int(DATE / 10000),
                     int(TIME / 10000),
                     int((TIME - int(TIME / 10000) * 10000) / 100),
                     int(TIME - int(TIME / 100) * 100),
                     0, 0, 0)
    return int(time.mktime(utc_tuple))


def datetime_to_timestamp(dt):
    """Converts a datetime object to UTC timestamp"""
    return int(utc_mktime(dt.timetuple()))


def normal_time_stamp(DATE):
    if 170101 < DATE < 180101:  # 年月日
        normal_time_stamp = (int(DATE / 10000) + 2000)*10000+(int((DATE - int(DATE / 10000) * 10000) / 100))*100+int(DATE - int(DATE / 100) * 100)

    else:   # 日月年
        normal_time_stamp = ((int(DATE - int(DATE / 100) * 100) + 2000))*10000+(int((DATE - int(DATE / 10000) * 10000) / 100))*100+int(DATE / 10000)

    return normal_time_stamp
