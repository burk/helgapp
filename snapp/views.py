from django.shortcuts import render
from snapp.models import Snap
from django.http import HttpResponseRedirect

def rate(request):
    k = 64

    win_name = request.POST.get("win", "")
    lose_name = request.POST.get("lose", "")

    win = Snap.objects.get(filename=win_name)
    lose = Snap.objects.get(filename=lose_name)

    ewin = 1.0 / (1.0 + 10.0**((lose.rating - win.rating)/400.0))
    elose = 1.0 - ewin

    win.rating += k * (1.0 - ewin)
    lose.rating += k * (0.0 - elose)

    win.save()
    lose.save()

    return HttpResponseRedirect('/')
    
