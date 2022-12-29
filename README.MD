# Decorator for measuring the execution time of a callable

```python

$pip install measure-exec-time
from measure_exec_time import measure_time
from time import sleep



@measure_time
def foo1():
    sleep(2)
    return 22





@measure_time(show_timedelta=False, show_start_end=True)
def foo2():
    sleep(2)
    return 22





@measure_time(show_timedelta=True, show_start_end=False)
def foo3():
    sleep(2)
    return 22


foo1()
print('----------')
foo2()
print('----------')
foo3()


    
```
<img src="https://github.com/hansalemaos/screenshots/raw/main/timemea.png"/>




