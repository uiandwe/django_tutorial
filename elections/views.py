from django.shortcuts import render
from django.http import HttpResponse

from .models import Candidate

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates' : candidates} #context에 모든 후보에 대한 정보를 저장
    return render(request, 'elections/index.html', context) # context로 html에 모든 후보에 대한 정보를 전달