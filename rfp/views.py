from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate, login
from django.forms.models import model_to_dict

from user_profile.models import UserProfile

from models import Project,Review,RequestForProposal,RfpCampaign,File_Test,ProposedReviewer,BudgetLine
from forms import ProjectForm,file_test,UpdateForm,ReviewForm,ProposedReviewerFormSet,ProposedReviewerForm,HRBudgetLineFormSet,EQBudgetLineFormSet,OCBudgetLineFormSet
from django.core.urlresolvers import reverse

def is_reviewer(User):
    return User.groups.filter(name='Reviewer').exists()

def is_pi(User):
    return User.groups.filter(name = 'Principal_Investigator').exists()

def get_absolute_url(view,object):
          return reverse('view', args=[str(object.id)])


def budget_line_sum(budget_list):
    total_budgeted = 0

    for line in budget_list :
        bl_dict = model_to_dict(line)
        total_budgeted += int(bl_dict["amount"])
    return total_budgeted
# Create your views here.

#@login_required(login_url='/login/')
@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def create_project(request):
    context = RequestContext(request)
    user = request.user

    if request.method == 'POST':
        p = ProjectForm(request.POST,request.FILES)

        if p.is_valid():
           p.save (commit=False)
           p.user = user.pk
           project = p.save()

           return HttpResponseRedirect(reverse('propose_reviewer', args=[project.pk]))

    else:
        p = ProjectForm()

    return render_to_response('rfp/create_project.html',{'form' : p, 'user' : user}, context)

#@user_passes_test(is_reviewer,login_url='/login/',redirect_field_name='next')

def post_review(request,projectId):
    context = RequestContext(request)
    user = request.user
    user_profile = UserProfile.objects.get(user = user.pk)
    project = Project.objects.get( pk = projectId)
    review = Review.objects.get(user = user.pk, project = project.pk)

    if request.method == 'POST':
        r = ReviewForm(request.POST,request.FILES,instance = review)

        if r.is_valid:
            r.save()
            url = ('../../../user_profile/profile')

            return HttpResponseRedirect(url)

    else:
        r = ReviewForm(instance = review)

    return render_to_response('rfp/post_review.html',{'form' : r, 'project' : project, 'user' : user, 'up' : user_profile}, context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def edit_project(request,projectId):
    context = RequestContext(request)
    user=request.user
    project = Project.objects.get( pk = projectId )

    if request.method == 'POST':
        p = UpdateForm(request.POST,request.FILES,instance=project)

        if p.is_valid():
           p.save()

           url = ('../../'+ projectId + "/")

           return HttpResponseRedirect(url)

    else:
        p = UpdateForm(instance=project)

    context_dict={'project' : project,'user' : user,'form' : p}

    return render_to_response('rfp/edit_project.html',context_dict,context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def project_detail(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)

    project_data = UpdateForm(data=model_to_dict(project))
    prop_rev_list = ProposedReviewer.objects.filter(project = project)
    budget_line_list = BudgetLine.objects.filter(project = project)
    hr_budget_line_list = BudgetLine.objects.filter(project = project,category = 'HR')
    oc_budget_line_list = BudgetLine.objects.filter(project = project,category = 'OC')
    eq_budget_line_list = BudgetLine.objects.filter(project = project,category = 'EQ')

    is_p = is_pi(user)
    is_rev = is_reviewer(user)
    oc_total = budget_line_sum(oc_budget_line_list)
    hr_total = budget_line_sum(hr_budget_line_list)
    eq_total = budget_line_sum(eq_budget_line_list)
    total = oc_total + hr_total + eq_total

    context_dict={'project' : project,'user' : user,'project_data' : project_data,'is_pi': is_p, 'bl' : budget_line_list,
    'is_rev' : is_rev, 'prop_rev_list' : prop_rev_list,
    'hr_budget_lines_list' : hr_budget_line_list, 'oc_budget_lines_list' : oc_budget_line_list,
    'eq_budget_lines_list' : eq_budget_line_list,
   'oc_total' : oc_total, 'hr_total' : hr_total, 'eq_total' : eq_total, 'total' : total}

    return render_to_response('rfp/project_details.html',context_dict,context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def propose_reviewer(request,projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get( pk = projectId )

    if request.method == 'POST':
        r = ProposedReviewerFormSet(request.POST)
        if r.is_valid():
           reviewers = r.save(commit = False)
           for rev in reviewers:
               rev.project = project
               rev.save()

           return HttpResponseRedirect(reverse('user_profile'))

    else:
        r = ProposedReviewerFormSet(queryset=ProposedReviewer.objects.filter(project = project.id))

    return render_to_response('rfp/propose_reviewer.html',{'formset' : r, 'user' : user, 'project' : project}, context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def edit_reviewer(request,proposedreviewerId):
    context = RequestContext(request)
    user = request.user
    prop_rev = ProposedReviewer.objects.get( pk = proposedreviewerId )
    project = Project.objects.get(pk = prop_rev.project.pk)

    if request.method == 'POST':
        r = ProposedReviewerForm(request.POST, instance = prop_rev)
        if r.is_valid():
            r.save()

            return HttpResponseRedirect(reverse('project_detail', args = [prop_rev.project.pk]))
    else:
        r = ProposedReviewerForm(instance= prop_rev)

    return render_to_response('rfp/edit_proposed_reviewer.html', {'f' : r, 'project' : project, 'user' : user, 'prop_rev' : prop_rev},context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def add_unique_reviewer(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)

    if request.method == 'POST':
        r = ProposedReviewerForm(request.POST)
        if r.is_valid():
            reviewer = r.save(commit = False)
            reviewer.project = project
            reviewer.save()

            return HttpResponseRedirect(reverse('project_detail', args = [project.pk]))
    else:
        r = ProposedReviewerForm()

    return render_to_response('rfp/add_unique_review.html', {'f' : r, 'project' : project, 'user' : user},context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def add_budget(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)

    if request.method == 'POST':
        hr = HRBudgetLineFormSet(request.POST,prefix='hr')
        eq = EQBudgetLineFormSet(request.POST,prefix='eq')
        oc = OCBudgetLineFormSet(request.POST,prefix='oc')

        if hr.is_valid() and eq.is_valid() and oc.is_valid():
            hrlines = hr.save(commit=False)
            for line in hrlines:
                line.project = project
                line.category = 'HR'
                line.save()
            for obj in hr.deleted_objects:
                obj.delete()


            eqlines = eq.save(commit=False)
            for line in eqlines:
                line.project = project
                line.category = 'EQ'
                line.save()

            for obj in eq.deleted_objects:
                obj.delete()

            oclines = oc.save(commit=False)
            for line in oclines:
                line.project = project
                line.category = 'OC'
                line.save()

            for obj in oc.deleted_objects:
                obj.delete()

        return HttpResponseRedirect(reverse('project_detail', args = [project.pk]))

    else:
        hr = HRBudgetLineFormSet(prefix = 'hr', queryset=BudgetLine.objects.filter(category='HR', project = project))
        eq = EQBudgetLineFormSet(prefix = 'eq', queryset=BudgetLine.objects.filter(category='EQ', project = project))
        oc = OCBudgetLineFormSet(prefix = 'oc', queryset=BudgetLine.objects.filter(category='OC', project = project))

    return render_to_response('rfp/add_budget.html',{'hr_formset' : hr,'eq_formset' : eq, 'oc_formset' : oc, 'user' : user, 'project' : project},context)


@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def prop_reviewer_list(request,projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get( pk = projectId )

    prop_rev_list = ProposedReviewer.objects.filter(project = project)

    return render_to_response('rfp/list_of_proposed_reviewer.html', {'user' : user, 'project' : project, 'proposed_reviewers' : prop_rev_list}, context)

def rfp_campaign(request,rfpcampaignId):
    context = RequestContext(request)
    user = request.user
    rfp_campaign=RfpCampaign.objects.get(id=rfpcampaignId)

    context_dict = {'user':user,'rfp_campaign':rfp_campaign}

    return render_to_response('rfp/rfp_details.html',context_dict,context)

def rfp_list(request):
    context= RequestContext(request)

    rfp_list = RequestForProposal.objects.all()
    rfp_c = RfpCampaign.objects.all()

    context_dict = {'rfp_list': rfp_list, 'rfp_c' : rfp_c}

    return render_to_response('rfp/rfp_list.html',context_dict,context)

def test_file(request):
    context= RequestContext(request)

    if request.method == 'POST':
        f = file_test(request.POST, request.FILES)
        if f.is_valid():
                name = f.cleaned_data['name']
                new_doc=File_Test(name=name)
                new_doc.save()
                print('Doc is created')

                instance = File_Test(document=request.FILES['document'])
                instance.save()
                print('Document is added')

                return HttpResponse('File Saved !!')
    else:
        f = file_test()

    context_dict = {'form' : f }
    return render_to_response('rfp/file_test.html',context_dict,context)