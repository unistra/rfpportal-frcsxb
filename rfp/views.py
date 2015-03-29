from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate, login

from models import Project,Review,RequestForProposal,RfpCampaign
from forms import ProjectForm

# Create your views here.

@login_required(login_url='/login/')
def create_project(request):
    context = RequestContext(request)
    user = request.user

    #p = ProjectForm(request.POST)

    if request.method == 'POST':
        p = ProjectForm(request.POST)

        if p.is_valid():
           name = p.cleaned_data['name']
           rfp_id = p.cleaned_data['rfp_id']
           rfp = RfpCampaign.objects.get(id = rfp_id)

           new_project = Project.objects.get_or_create(name=name,rfp=rfp,user=user)

           return HttpResponseRedirect('../profile/')

           #new_project.save()
           #new_project.save(commit=True)
    else:
        ProjectForm()

    return render_to_response('rfp/create_project.html',{'form' : ProjectForm}, context)


@login_required(login_url='/login/')
def post_review(request):
    context = RequestContext(request)
    user = request.user

    p = ProjectForm(request.POST)

    if request.method == 'POST':
        p = ProjectForm(request.POST)

        if p.is_valid:
            new_project = p.save(commit=False)
            new_project.user_id = user.id

            new_project.save()
    else:
        ProjectForm()

    return render_to_response('rfp/post_review.html',{'form' : ProjectForm}, context)

