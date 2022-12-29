from datetime import datetime
from functools import wraps
from cprinter import TC


def measure_time(f_py=None, show_timedelta=True, show_start_end=True):

    assert callable(f_py) or f_py is None

    def _decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            a_ts = datetime.now()

            vala = func(*args, **kwargs)
            t_ts = datetime.now()
            if show_start_end:
                print(TC(f"Start:     {a_ts}").bg_black.fg_lightgreen)
                print(TC(f"End:       {t_ts}").bg_black.fg_yellow)
            if show_timedelta:
                print(TC(f"Timedelta: {t_ts - a_ts}").bg_black.fg_pink)

            return vala

        return wrapper

    return _decorator(f_py) if callable(f_py) else _decorator

