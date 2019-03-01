from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Question

import requests

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
# Create your views here.
def detail(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html',{"question":question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index2(request):
    return render(request, 'polls/index2.html')

def crawling(request):
    req = requests.get('https://beomi.github.io/beomi.github.io_old/')
    html  = req.text
    # return HttpResponse(html)

    sampleDict = {"두산" : 2,"투수" : 120, "타자" : 25}
    context = {'dict': sampleDict}
    return render(request, 'polls/crawling.html', context)
