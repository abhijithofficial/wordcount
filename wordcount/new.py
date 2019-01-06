from django.http import HttpResponse
from django.shortcuts import render
import operator
def count(request):
    fulltext=request.GET['name']
    fulltext=fulltext.split()
    worddict={}
    for word in fulltext:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
    sorterlar=sorted(worddict.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{'full':len(fulltext),'give':fulltext,'worditem':worddict.items(),'large':sorterlar})
