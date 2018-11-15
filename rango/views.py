from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page
from rango.forms import CategoryForm
from rango.forms import PageForm

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

def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    return render(request, 'rango/add_category.html', {'form': form})

    
def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None
    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if category:
                page = form.save(commit=False)
                page.category = category
                page.views = 0
                page.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)
    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
