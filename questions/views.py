#coding=utf-8
from django.shortcuts import render
from models import *
import cgi

# Create your views here.
def showAll(request):
    orgin=Question.objects.all()
    for obj in orgin:
        temp=obj.options.replace('[','').replace(']','').split(',')
        obj.options=temp
    return render(request,'questions/showAll.html',{'list':orgin})

def answer(request):
    data=request.GET.dict().iteritems()
    result=0
    for k,v in data:
        if isRight(k,v[1:2]):
            result+=10
    print(result)
    return render(request,'questions/answer.html',{'result':result})

def isRight(id,result):
    return Question.objects.get(id=id).answer.encode('utf-8')==result.encode('utf-8')