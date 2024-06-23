from django.shortcuts import render
from Category.models import Maincategory,Subcategory
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import  login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.template import loader
from django.urls import reverse
# Create your views here. +
@login_required
def addcategory(request):
    if(request.method=="POST"):
        categoryname=request.POST['name']
        categorydesc=request.POST['desc']
        c=Maincategory.objects.create(name=categoryname,desc=categorydesc)
        c.save()
        return viewmaincategory(request)
    return render(request,template_name='addcategory.html')
@login_required
def addsubcategory(request):
    cn = Maincategory.objects.all()
    if(request.method == "POST"):
        cat_id = request.POST['category']
        subcatname = request.POST['sname']
        subcatdesc = request.POST['sdesc']
        image   = request.FILES['image']
        category = Maincategory.objects.get(id=cat_id)
        s = Subcategory.objects.create(maincategory=category,sname=subcatname, sdesc=subcatdesc,simages=image)
        s.save()
        return viewsubcategory(request)

    return render(request, template_name='addsubcategory.html',context={'cn':cn})
@login_required
def viewmaincategory(request):
    v = Maincategory.objects.all()

    return render(request,template_name='viewmaincategory.html',context={'v':v})
@login_required
def deletemaincategory(request):
    v = Maincategory.objects.all()

    return render(request, template_name='deletemaincategory.html', context={'v': v})
@login_required
def delmaincategory(request,p):
    b=Maincategory.objects.get(id=p)
    b.delete()
    return deletemaincategory(request)
@login_required
def viewupdatemaincategory(request):
    v = Maincategory.objects.all()

    return render(request, template_name='viewupdatemaincategory.html', context={'v': v})
@login_required
def updatemaincategory(request,p):
    v= Maincategory.objects.get(id=p)
    template = loader.get_template('updatemaincategory.html')
    context = {'v': v}
    return HttpResponse(template.render(context, request))
@login_required
def updaterecord(request, p):
  name = request.POST['name']
  desc = request.POST['desc']
  v = Maincategory.objects.get(id=p)
  v.name = name
  v.desc = desc
  v.save()
  return viewupdatemaincategory(request)

@login_required
def viewsubcategory(request):
    vs = Subcategory.objects.all()

    return render(request,template_name='viewsubcategory.html', context={'vs': vs})
@login_required
def deletesubcategory(request):
    ds = Subcategory.objects.all()

    return render(request, template_name='deletesubcategory.html', context={'ds': ds})

@login_required
def delsubcategory(request,p):
    b=Subcategory.objects.get(id=p)
    b.delete()
    return deletesubcategory(request)
@login_required
def viewupdatesubcategory(request):
    v = Subcategory.objects.all()

    return render(request, template_name='viewupdatesubcategory.html', context={'v': v})
@login_required
def updatesubcategory(request,p):
    v= Subcategory.objects.get(id=p)
    template = loader.get_template('updatesubcategory.html')
    context = {'v': v}
    return HttpResponse(template.render(context, request))
@login_required
def updatesubrecord(request, p):
  cname = request.POST['category']
  name = request.POST['sname']
  desc = request.POST['sdesc']
  image = request.FILES['image']
  v = Subcategory.objects.get(id=p)
  # v.maincategory=cname
  v.sname = name
  v.sdesc = desc
  v.simages = image

  v.save()
  return viewupdatesubcategory(request)
