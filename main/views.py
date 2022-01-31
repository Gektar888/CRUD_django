from django.shortcuts import render
from .forms import BlogForm
from .models import Blog
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)



def update_view(request, id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id=id)

    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "main/update.html", context)

def create(request):
    context = {}
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request,'main/create.html',context)

def list(request):
    context = {}
    context['dataset'] = Blog.objects.all()
    return render(request,'main/list.html',context)

def detail(request,id):
    context = {}

    context["data"] = Blog.objects.get(id=id)

    return render(request, "main/detail.html", context)
# Create your views here.
