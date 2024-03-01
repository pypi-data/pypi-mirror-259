# from dateroll.date.date import Date
# from dateroll.duration.duration import Duration
# from dateroll.schedule.schedule import Schedule
# from dateroll.ddh.ddh import ddh, calmath, cals


import sys
import traceback

try:
    from dateroll.date.date import Date
    from dateroll.ddh.ddh import calmath, cals, ddh
    from dateroll.duration.duration import Duration
    from dateroll.schedule.schedule import Schedule

    cals.load_sample_data()
    ddh("t+3m1bd|NYuLN")
    print("asdfasdf", sys.version.split(" ")[0], "✅" * 30)
except Exception as e:
    print("asdfasdf", sys.version.split(" ")[0], "❌" * 30, str(e))
