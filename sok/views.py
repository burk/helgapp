from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import Application
from forms import ApplicationForm

@login_required
def applications(request):
    apps = Application.objects.filter(user=request.user)
    return render(request, 'sok/applications.html', {'applications': apps})

@login_required
def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return HttpResponseRedirect(reverse('applications'))
    else:
        form = ApplicationForm()
    return render(request, 'sok/apply.html', {'form': form})

