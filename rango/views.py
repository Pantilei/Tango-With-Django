from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict={'boldmessage':"Crunchy, creamy, cookie, candy, cupcake!"}
    return render(request,'rango/index.html', context=context_dict)
    #return HttpResponse("HI bro!!!")
def about(request):
    output={'message':"This page has been put together by Pantilei"}
    return render(request,"rango/about.html",context=output)
