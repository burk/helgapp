from django.shortcuts import render
from datetime import datetime
import time

def index(request):
    fmt = '%Y-%m-%d %H:%M:%S'
    now   = datetime.now()
    start = datetime.strptime('2013-08-01 12:00:00', fmt)
    end   = datetime.strptime('2013-10-07 12:00:00', fmt)

    now   = time.mktime(now.timetuple())
    start = time.mktime(start.timetuple())
    end   = time.mktime(end.timetuple())

    return render(request, 'landingpage/index.html',
            {'progress': 100 * (end - now) / (end - start)}
    )

