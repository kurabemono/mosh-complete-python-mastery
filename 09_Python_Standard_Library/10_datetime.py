from datetime import datetime
import time

dt1 = datetime(2023, 4, 5)
dt2 = datetime.now()
datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))
print(dt2 > dt1)
