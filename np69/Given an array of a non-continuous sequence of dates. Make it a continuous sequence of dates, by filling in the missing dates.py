import numpy as np
dates = np.arange(np.datetime64('2018-02-01'), np.datetime64('2018-02-25'), 2)
print('original:',dates)
filled_in = np.array([np.arange(date, (date+d)) for date, d in zip(dates, np.diff(dates))]).reshape(-1)
# add the last day
output = np.hstack([filled_in, dates[-1]]) #horizontal stack
"""
#or
out = []
for date, d in zip(dates, np.diff(dates)):
    out.append(np.arange(date, (date+d)))

filled_in = np.array(out).reshape(-1)

# add the last day
output = np.hstack([filled_in, dates[-1]])
"""
print(output)

"""
.zip function join two arrays together.
"""