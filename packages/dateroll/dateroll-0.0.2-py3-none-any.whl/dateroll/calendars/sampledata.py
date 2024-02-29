import pathlib
import pickle
import datetime

from dateutil.relativedelta import relativedelta as rd

DEFAULT_YEAR_RANGE = 200

def generate_ALL_and_WE(n=DEFAULT_YEAR_RANGE):
    """
    generate set of all days in some "big range"
    generate set of holidays where holiday is saturday or sunday in some "big range"
    return both sets
    """
    t_start = datetime.date.today() - rd(years=n)
    t_end = datetime.date.today() + rd(years=n)

    t = t_start
    ALL = set()
    WE = set()
    while t < t_end:
        ALL |= {
            t,
        }
        if t.weekday() in (5, 6):
            WE |= {
                t,
            }
        t += rd(days=1)

    return ALL, WE

def load_sample_data(cals, n=DEFAULT_YEAR_RANGE):
    ALL, WE = generate_ALL_and_WE(n)

    filename = pathlib.Path(__file__).parents[0] / 'sampledata.pkl'
    if filename.exists():
        with open(filename,'rb') as f:
            sample_data = pickle.load(f)
    else:
        raise FileNotFoundError(filename)

    sample_data.update({'ALL':ALL,'WE':WE})

    for i in ("ALL","WE","NY","LN","BR","ECB","FED"):
        if i not in cals:
            cals[i] = sample_data[i]
        else:
            print(f'[dateroll] {i} exists, skipping over.')
   
if __name__ == "__main__":
    from dateroll.calendars.calendars import Calendars

    cals = Calendars()

    load_sample_data(cals, n=200)
