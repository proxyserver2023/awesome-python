"""
>>> timedelta(hours=5)
Out[3]: datetime.timedelta(0, 18000)
>>> _
Out[4]: datetime.timedelta(0, 18000)
>>> print(_)
5:00:00
>>> timedelta(hours=6)
Out[6]: datetime.timedelta(0, 21600)
>>> print(_)
6:00:00
>>> timedelta(hours=-5)
Out[8]: datetime.timedelta(-1, 68400)
>>> print(_)
-1 day, 19:00:00

>>> year = timedelta(days=365)
Out[9]: datetime.timedelta(365)
>>> print(_)
365 days, 0:00:00
>>> another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
>>> print(_)
365 days, 0:00:00
>>> year.total_seconds()
31536000.0
>>> year == another_year
True
>>> ten_years = 10 * year
>>> ten_years, ten_years.days // 365
(datetime.timedelta(days=3650), 10)
>>> nine_years = ten_years - year
>>> nine_years, nine_years.days // 365
(datetime.timedelta(days=3285), 9)
>>> three_years = nine_years // 3
>>> three_years, three_years.days // 365
(datetime.timedelta(days=1095), 3)
>>> abs(three_years - ten_years) == 2 * three_years + year
True
"""
