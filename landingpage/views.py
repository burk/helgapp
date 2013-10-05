from django.shortcuts import render
from datetime import datetime
from snapp.models import Snap
import random
import time

def index(request):
    fmt = '%Y-%m-%d %H:%M:%S'
    now   = datetime.now()
    start = datetime.strptime('2013-10-01 12:00:00', fmt)
    end   = datetime.strptime('2013-10-07 12:00:00', fmt)

    now   = time.mktime(now.timetuple())
    start = time.mktime(start.timetuple())
    end   = time.mktime(end.timetuple())

    snaps = Snap.objects.filter(censored=False).order_by('-downloaded')

    progress_text = random.choice([
            'Reticulating splines',
            'Herding llamas',
            'Precaching resources',
            'Loading...',
            ])

    return render(request, 'landingpage/index.html', {
        'progress_text': progress_text,
        'progress': 100 * (1 - (end - now) / (end - start)),
        'snaps': snaps,
        })

