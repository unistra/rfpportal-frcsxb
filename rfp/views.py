from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate, login
from django.forms.models import model_to_dict

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
           requested_amount=p.cleaned_data['requested_amount']
           starting_date=p.cleaned_data['starting_date']
           project_duration=p.cleaned_data['project_duration']
           ending_date=p.cleaned_data['ending_date']
           purpose=p.cleaned_data['purpose']
           scope_of_work=p.cleaned_data['scope_of_work']
           anticipated_impact=p.cleaned_data['anticipated_impact']
           rfp_id = p.cleaned_data['rfp_id']
           rfp = RfpCampaign.objects.get(id = rfp_id)

           new_project = Project.objects.get_or_create(name=name,rfp=rfp,user=user,requested_amount=requested_amount,starting_date=starting_date,project_duration=project_duration,
                                                       ending_date=ending_date,purpose=purpose,scope_of_work=scope_of_work,anticipated_impact=anticipated_impact)

           url=('../../user_profile/profile/')

           return HttpResponseRedirect(url)

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


@login_required(login_url='/login/')
def project_detail(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)

    if request.method == 'POST':
        p = ProjectForm(request.POST)

        if p.is_valid():
           name = p.cleaned_data['name']
           requested_amount=p.cleaned_data['requested_amount']
           starting_date=p.cleaned_data['starting_date']
           project_duration=p.cleaned_data['project_duration']
           ending_date=p.cleaned_data['ending_date']
           purpose=p.cleaned_data['purpose']
           scope_of_work=p.cleaned_data['scope_of_work']
           anticipated_impact=p.cleaned_data['anticipated_impact']
           rfp_id = p.cleaned_data['rfp_id']
           rfp = RfpCampaign.objects.get(id = rfp_id)

           updated_project = Project(id=projectId,name=name,rfp=rfp,user=user,requested_amount=requested_amount,starting_date=starting_date,project_duration=project_duration,
                                                       ending_date=ending_date,purpose=purpose,scope_of_work=scope_of_work,anticipated_impact=anticipated_impact)

           updated_project.save(update_fields=['name','requested_amount','starting_date','project_duration','ending_date','purpose','scope_of_work','anticipated_impact'])

           def get_absolute_url(self):
                from django.core.urlresolvers import reverse
                return reverse('rfp.views.project_detail', args=[str(self.id)])

           get_absolute_url(project)
           url=get_absolute_url(project)

           return HttpResponseRedirect(url)

    else:
        project=Project.objects.get(id=projectId)
        project_dict=model_to_dict(project)

        form = ProjectForm(project_dict)


    context_dict={'project':project,'user':user,'form':form}

    return render_to_response('rfp/project_details.html',context_dict,context)