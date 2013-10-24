from django.shortcuts import render
from datetime import datetime
from snapp.models import Snap
import random
import time

def index(request):
    goal = 150

    left, right = Snap.objects.filter(censored=False).order_by('?')[0:2]

    snaps = Snap.objects.filter(censored=False).order_by('-downloaded')[:10]

    count = Snap.objects.count()

    progress_text = random.choice([
            'Reticulating splines',
            'Herding llamas',
            'Precaching resources',
            'Loading...',
            ])

    return render(request, 'landingpage/index.html', {
        'progress_text': progress_text,
        'progress': 100 * float(count) / float(goal),
        'snaps': snaps,
        'snap_left': left,
        'snap_right': right,
        })

