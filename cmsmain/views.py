from django.shortcuts import render
from django.http import HttpResponse
from .models import Projects
# Create your views here.

def index(request):
    project_list = Projects.objects.order_by('pub_date')[:5]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html',context)

def add(request):
    return render(request, 'projects/add.html')

def processAdd(request):
    fname = request.POST.get('fname')
    fname = request.POST.get('lname')
    fname = request.POST.get('email')
    fname = request.POST.get('position')
    if request.FILES.get('image'):
        user_pic = request.FILE.get('image')
    else:
        user_pic = 'profile/image.jpg'
    try:
        n = 
