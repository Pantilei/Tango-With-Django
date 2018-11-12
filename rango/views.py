from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories': category_list, 'pages':page_list}
    return render(request,'rango/index.html', context_dict)
    #return HttpResponse("HI bro!!!")
def about(request):
    output={'message':"This page has been put together by Pantilei"}
    return render(request,"rango/about.html",context=output)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug = category_name_slug)
        print(Category.objects)
        print(category)
        pages = Page.objects.filter(category = category)
        print(pages)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context_dict)
