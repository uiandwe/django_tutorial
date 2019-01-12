from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

def index(request):
    candidates = Candidate.objects.all()
    return render(request, 'elections/index.html')