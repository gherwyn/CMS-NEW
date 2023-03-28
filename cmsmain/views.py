from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Projects
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    project_list = Projects.objects.order_by('pub_date')[:5]
    context = {'project_list': project_list}
    return render(request, 'projects/index.html',context)

def add(request):
    return render(request, 'projects/add.html')

def processadd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    position = request.POST.get('position')
    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile/image.jpg'
    try:
        n = Projects.objects.get(user_email=email)
        # number already exists
        return render(request, 'projects/add.html', {
            'error_message': "Duplicated email: " + email
        })
    except ObjectDoesNotExist:
        user = Projects.objects.create(user_email=email, user_fname=fname, user_lname=lname, user_position=position, user_image=user_pic)
        user.save()
        return HttpResponseRedirect('/cmsmain')