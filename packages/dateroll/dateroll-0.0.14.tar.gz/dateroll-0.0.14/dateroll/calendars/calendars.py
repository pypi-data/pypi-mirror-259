import datetime
import hashlib
import os
import pathlib
import sys
import shelve
import glob
import pickle
from contextlib import ContextDecorator

PARENT_LOCATION = pathlib.Path.home() / ".dateroll/"
PARENT_LOCATION.mkdir(exist_ok=True)
MODULE_LOCATION = PARENT_LOCATION / "calendars/"
MODULE_LOCATION.mkdir(exist_ok=True)
DATA_LOCATION_FILE = MODULE_LOCATION / "holiday_lists"

class Shelf:
    def __enter__(self,filename):
        if pathlib.path(filename).exists():
            self.filename = filename
            with open(filename,'rb') as f:    
                self.data = pickle.load(f)
        else:
            self.filename = filename
            self.data = {}
        return self.data
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            with open(self.filename,'wb') as f:
                    pickle.dump(self.data,f)
        else:
            return True


class Calendars:
    def __init__(self, home=DATA_LOCATION_FILE):
        self.home = str(home)

        with shelve.open(self.home) as db:
            if "WE" not in db and "ALL" not in db:
                self.load_all_and_we()

    def keys(self):
        with shelve.open(self.home) as db:
            return list(db.keys())

    @property
    def hash(self):
        '''
        need to use glob to find file because behavior of shelve across users
        '''
        filenames = glob.glob(f'{self.home}*')
        if len(filenames)==1:
            filename = filenames[0]
        else:
            raise FileNotFoundError(self.home)
        with open(filename, "rb") as f:
            return hashlib.md5(
                f.read(),
            ).hexdigest()

    def __setitem__(self, k, v):
        from dateroll.calendars.calendarmath import \
            DATA_LOCATION_FILE as calendar_math_file

        if calendar_math_file.exists():
            os.remove(calendar_math_file)

        # key must be 2-3 letter string in uppercase
        if not isinstance(k, str):
            raise Exception(f"Cal name must be string (got {type(k).__name__})")
        if len(k) < 2 or len(k) > 3:
            raise Exception(f"Cal name be 2 or 3 charts (got {len(k)})")
        if not k.isupper():
            raise Exception(f"Cal name must be all uppercase")
        # value must be a list of dates
        if not isinstance(v, (set, list, tuple)):
            raise Exception(
                f"Cal values must be a set/list/tuple (got {type(v).__name__})"
            )

        processed = []
        for i in v:
            if isinstance(i, datetime.datetime):
                dt = datetime.date(i.year, i.month, i.day)
                processed.append(dt)
            elif isinstance(i, datetime.date):
                dt = i
                processed.append(dt)
            elif hasattr(type(i),'__class__') and type(i).__class__.__name__ == 'Date':
                dt = dt.date
                processed.append(dt)
            else:
                raise Exception(
                    f"All cal dates must be of dateroll.Date or datetime.date{{time}} (got {type(i).__name__})"
                )

        with shelve.open(self.home) as db:
            if k in db.keys():
                raise Exception(
                    f"{k} exists already, delete first.if you want to replace."
                )
            s = list(sorted(list(set(processed))))
            db[k] = s

    def __getitem__(self, k):
        return self.get(k)

    def __getattr__(self, k):
        '''
        allows for dot notation
        '''
        if k in('hash','home'):
            return super().__getattribute__(k)
        else:
            return self.get(k)

    def __contains__(self, k):
        with shelve.open(self.home) as db:
            return str(k) in db

    def __delitem__(self, k):
        with shelve.open(self.home) as db:
            del db[k]

    def get(self, k):
        with shelve.open(self.home) as db:
            return db[k]

    def clear(self):
        with shelve.open(self.home) as db:
            db.clear()

    def __repr__(self):
        self.info
        return f'{self.__class__.__name__}(home="{self.home}")'

    def load_all_and_we(self):
        from dateroll.calendars.sampledata import generate_ALL_and_WE

        ALL, WE = generate_ALL_and_WE()
        self["ALL"] = ALL
        self["WE"] = WE

    def load_sample_data(self):
        from dateroll.calendars.sampledata import load_sample_data as lsd
        lsd(self)
        self.info

    @property
    def info(self):
        pattern = lambda a,b,c,d: f'{a:6}|{b:>8}|{c:12}|{d:12}'
        with shelve.open(self.home) as db:
            stats = []
            print(pattern('name','#dates','min date','max date'))
            print(pattern('-'*6,'-'*8,'-'*12,'-'*12))
            for i in db.keys():
                l = db.get(i)
                if len(l)>0:
                    n = len(l)
                    mn = min(l)
                    mx = max(l)
                else:
                    n,mn,mx = 0,None,None
                print(pattern(str(i),str(n),str(mn),str(mx)))


if __name__ == "__main__":
    cals = Calendars()
    cals.load_sample_data()

    # import code;code.interact(local=locals())
