from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import Projects
from django.core.paginator import Paginator
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    project_list = Projects.objects.all().order_by('-pub_date')
    
    paginator = Paginator(project_list, 5)

    page_number = request.GET.get('page')

    project_list = paginator.get_page(page_number)

    return render(request, 'projects/index.html', { 'page_obj': project_list })

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

def detail(request, projects_id):
    try:
        projects = Projects.objects.get(pk=projects_id)
    except Projects.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'projects/detail.html', {'projects': projects})

def delete(request, projects_id):
    Projects.objects.filter(id=projects_id).delete()
    return HttpResponseRedirect('/cmsmain')

def edit(request, projects_id):
    try:
        projects = Projects.objects.get(pk=projects_id)
    except Projects.DoesNotExist:
        raise Http404("Profile does not exist")
    return render(request, 'projects/edit.html', {'projects': projects})

def processedit(request, projects_id):
    user = get_object_or_404(Projects, pk=projects_id)
    projects_pic = request.FILES.get('image')
    try:
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        position = request.POST.get('position')
    except (KeyError, Projects.DoesNotExist):
        return render(request, 'cmsmain/detail.html', {
            'projects': Projects,
            'error_message': "Problem updating record"
        })
    else:
        projects_info = Projects.objects.get(id=projects_id)
        projects_info.user_fname = fname
        projects_info.user_lname = lname
        projects_info.user_email = email
        projects_info.user_position = position
        if projects_pic:
            projects_info.user_image = projects_pic
        projects_info.save()
        return HttpResponseRedirect(reverse('cmsmain:detail' , args=(projects_id,)))