from django.http import HttpResponse
from django.shortcuts import render
def count(request):
    fulltext=request.GET['name']
    fulltext=fulltext.split()
    return render(request,'count.html',{'full':len(fulltext),'give':fulltext})
