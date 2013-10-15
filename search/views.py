from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render

def search(request):
    return render(request, "search/search.html")

