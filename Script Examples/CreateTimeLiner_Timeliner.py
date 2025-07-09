from datetime import datetime
from datetime import timedelta

# build period names from start to end
# set the periods from the beginning of the job to the end of the job
yr_beg = 2023
wk_beg = 51
yr_end = 2025
wk_end = 9
listof = []
for y in range(yr_beg, yr_end + 1):
    if yr_beg == yr_end:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(wk_beg, wk_end + 1)]
    elif y == yr_end:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(1, wk_end + 1)]
    elif y == yr_beg:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(wk_beg, 53 + 1)]
    else:
        wlist = [str(y)] + [str(y) + '.' + element.__str__() for element in range(1, 53 + 1)]
    listof.append(wlist)


#create time timeler entries to match up with search sets and link
#need to identify week beginning and ending dates for planned start/end
# dtStart = datetime.datetime.strptime("")
for y in listof:
    yr = y[0]
    for wk in y[1:]:
        d = wk
        # d = "2024.1"
        dtStart = datetime.strptime(d + '-1', "%Y.%W-%w") + timedelta(days=-1)
        dtEnd = dtStart + timedelta(days=6)
        print(dtEnd)