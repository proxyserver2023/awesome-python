```bash
mysql -uusername -ppassword # Login
mysql -uusername -ppassword < filename # Importing
mysqdump -uusername -ppassword database [tables] > filename # Dumping
```

```bash
# integer(maximum_value) -> int(5)
# float(maximum_value, upto_decimal_places) -> float(10, 4)
# double(maximum_value, upto_decimal_places) -> double(20,3)
# timestamp(maximum_value) -> timestamp(8) -> timestamp(YYYYMMDD)
#                          -> timestamp(12) ->                             
# char(maximum_value)      -> char(10)
# varchar(maximum_value)   -> varchar(20)
# blob                     -> blob
# enum

```

```
COUNT(column|*)
AVG(column)
MIN(column)
MIN()
MAX()
SUM()
abs()
round()
floor()
ceiling()
sqrt()
pow()
rand()
sin()
```

