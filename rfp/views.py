from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test

from django.forms.models import model_to_dict
import datetime

from user_profile.models import UserProfile

from models import Project,Review,RfpCampaign,File_Test,ProposedReviewer,BudgetLine
from forms import ProjectForm,file_test,UpdateForm,ReviewForm,ProposedReviewerFormSet,ProposedReviewerForm,BudgetLineEQ,BudgetLineHR,BudgetLineOP,ExcludedReviewerForm
from django.core.urlresolvers import reverse

def is_reviewer(User):
    return User.groups.filter(name='Reviewer').exists()

def is_pi(User):
    return User.groups.filter(name = 'Principal_Investigator').exists()

def is_pi_or_reviewer(User):
    state = False
    if is_pi(User) or is_reviewer(User):
        state = True
    return state

def is_staff(User):
    return User.is_staff

def get_absolute_url(view,object):
          return reverse('view', args=[str(object.id)])

def budget_line_sum(budget_list):
    total_budgeted = 0

    for line in budget_list :
        bl_dict = model_to_dict(line)
        total_budgeted += int(bl_dict["amount"])
    return total_budgeted

def get_custom_answers(review_dict,request):
                    dict = {}
                    for row in review_dict:
                        for p in request.POST:
                           if str(p) == row:
                                v = request.POST.get(p)
                                dict[str(row)] = v
                    return dict

def find_user_review_for_project(user,project):
        try:
            review=Review.objects.get(user=user,project=project)
        except Review.DoesNotExist:
            review={}

        return review

# Views start here.
@user_passes_test(is_pi,login_url='/login/')
def create_project(request):
    context = RequestContext(request)
    user = request.user
    progress_status = 30

    if request.method == 'POST':
        p = ProjectForm(request.POST,request.FILES)

        if p.is_valid():
           proj = p.save (commit=False)
           proj.user = user
           proj.status = 'pending'
           project = p.save()
           return HttpResponseRedirect(reverse('create_project_budget', args=[project.pk]))

    else:
        p = ProjectForm()

    return render_to_response('rfp/create_project.html',{'form' : p, 'user' : user, 'progress_status' : progress_status}, context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def create_project_budget(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)


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

    current_url = reverse('create_project_budget', args = [project.pk])

    context_dict={'project' : project,'user' : user,'is_pi': is_p, 'bl' : budget_line_list,
    'is_rev' : is_rev,'current_url' : current_url,
    'hr_budget_lines_list' : hr_budget_line_list, 'oc_budget_lines_list' : oc_budget_line_list,
    'eq_budget_lines_list' : eq_budget_line_list,
    'oc_total' : oc_total, 'hr_total' : hr_total, 'eq_total' : eq_total, 'total' : total}

    return render_to_response('rfp/create_project_budget.html',context_dict,context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def create_project_reviewer(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)

    project_data = UpdateForm(data=model_to_dict(project))
    prop_rev_list = ProposedReviewer.objects.filter(project = project)
    budget_line_list = BudgetLine.objects.filter(project = project)

    is_p = is_pi(user)
    is_rev = is_reviewer(user)
    current_url = reverse('create_project_reviewer', args = [project.pk])

    context_dict={'current_url' : current_url,'project' : project,'user' : user,'project_data' : project_data,'is_pi': is_p, 'bl' : budget_line_list,
    'is_rev' : is_rev, 'prop_rev_list' : prop_rev_list}

    return render_to_response('rfp/create_project_reviewer.html',context_dict,context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def create_project_summary(request,projectId):
    context = RequestContext(request)

    project = Project.objects.get(pk = projectId)
    project_data = UpdateForm(data=model_to_dict(project))

    budget_line_list = BudgetLine.objects.filter(project = project)
    hr_budget_line_list = BudgetLine.objects.filter(project = project,category = 'HR')
    oc_budget_line_list = BudgetLine.objects.filter(project = project,category = 'OC')
    eq_budget_line_list = BudgetLine.objects.filter(project = project,category = 'EQ')

    prop_rev_list = ProposedReviewer.objects.filter(project = project)
    total_budgeted = budget_line_sum(budget_line_list)

    project.send_project_confirmation_email()

    context_dict = {'project':project,'project_data' : project_data,'budget_line_list': budget_line_list,
                    'total' : total_budgeted,'hr_budget_lines_list' : hr_budget_line_list, 'oc_budget_lines_list' : oc_budget_line_list,
                    'eq_budget_lines_list' : eq_budget_line_list,'prop_rev_list' : prop_rev_list}

    return render_to_response('rfp/create_project_summary.html',context_dict,context)

@user_passes_test(is_pi,login_url='/login/',redirect_field_name='next')
def edit_project(request,projectId):
    context = RequestContext(request)
    user=request.user
    project = Project.objects.get( pk = projectId )

    if request.method == 'POST':
        p = UpdateForm(request.POST,request.FILES,instance=project)

        if p.is_valid():
           p.save()
           return HttpResponseRedirect(reverse('project_detail', args=[project.pk]))

    else:
        p = UpdateForm(instance=project)

    context_dict={'project' : project,'user' : user,'form' : p}

    return render_to_response('rfp/edit_project.html',context_dict,context)


@user_passes_test(is_pi_or_reviewer,login_url='/login/',redirect_field_name='next')
def project_detail(request,projectId):
    context = RequestContext(request)
    user = request.user
    is_p = is_pi(user)
    is_rev = is_reviewer(user)

    project=Project.objects.get(id=projectId)
    review = find_user_review_for_project(user,project)

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
    current_url = reverse('project_budget', args = [project.pk])

    context_dict={'project' : project,'user' : user,'project_data' : project_data,'is_pi': is_p, 'bl' : budget_line_list,
    'is_rev' : is_rev, 'prop_rev_list' : prop_rev_list,'current_url':current_url,'review':review,
    'hr_budget_lines_list' : hr_budget_line_list, 'oc_budget_lines_list' : oc_budget_line_list,
    'eq_budget_lines_list' : eq_budget_line_list,
   'oc_total' : oc_total, 'hr_total' : hr_total, 'eq_total' : eq_total, 'total' : total}

    return render_to_response('rfp/project_details.html',context_dict,context)

@user_passes_test(is_pi_or_reviewer,login_url='/login/',redirect_field_name='next')
def project_detail_budget(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)
    review = find_user_review_for_project(user,project)

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
    current_url = reverse('project_budget', args = [project.pk])

    context_dict={'project' : project,'user' : user,'is_pi': is_p, 'bl' : budget_line_list,
    'is_rev' : is_rev,'current_url' : current_url,
    'hr_budget_lines_list' : hr_budget_line_list, 'oc_budget_lines_list' : oc_budget_line_list,
    'eq_budget_lines_list' : eq_budget_line_list,'review' : review,
   'oc_total' : oc_total, 'hr_total' : hr_total, 'eq_total' : eq_total, 'total' : total}

    return render_to_response('rfp/project_details_budget.html',context_dict,context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def project_detail_reviewers(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)

    project_data = UpdateForm(data=model_to_dict(project))
    prop_rev_list = ProposedReviewer.objects.filter(project = project)
    budget_line_list = BudgetLine.objects.filter(project = project)

    is_p = is_pi(user)
    is_rev = is_reviewer(user)
    current_url = reverse('project_reviewer', args = [project.pk])

    context_dict={'current_url' : current_url,'project' : project,'user' : user,'project_data' : project_data,'is_pi': is_p, 'bl' : budget_line_list,
    'is_rev' : is_rev, 'prop_rev_list' : prop_rev_list}

    return render_to_response('rfp/project_details_reviewer.html',context_dict,context)

@user_passes_test(is_reviewer,login_url='/project/login_no_permission/',redirect_field_name='next')
def project_review(request,projectId):
    context = RequestContext(request)
    user = request.user
    project=Project.objects.get(id=projectId)
    review = Review.objects.get(project=projectId,user=user.pk)
    questions = project.rfp.get_questions()
    review_data = ReviewForm(data=model_to_dict(review),questions=questions)

    is_p = is_pi(user)
    is_rev = is_reviewer(user)
    current_url = reverse('project_reviewer', args = [project.pk])

    context_dict={'current_url' : current_url,'project' : project,'user' : user,'review_data' : review_data,
                  'is_pi': is_p,'is_rev' : is_rev,'review':review}

    return render_to_response('rfp/project_review.html',context_dict,context)



@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def edit_reviewer(request,proposedreviewerId):
    context = RequestContext(request)
    user = request.user
    prop_rev = ProposedReviewer.objects.get( pk = proposedreviewerId )
    project = Project.objects.get(pk = prop_rev.project.pk)
    alldata = request.POST
    redirect = alldata.get('redirect','0')

    if request.method == 'POST':

        if 'delete' in request.POST:
             prop_rev.delete()
             return HttpResponseRedirect(redirect)
        else:
            r = ProposedReviewerForm(request.POST, instance = prop_rev)

            if r.is_valid():
                r.save()

                return HttpResponseRedirect(redirect)

    else:
        r = ProposedReviewerForm(instance= prop_rev)

    return render_to_response('rfp/edit_proposed_reviewer.html', {'f' : r, 'project' : project, 'user' : user, 'prop_rev' : prop_rev},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def edit_excluded_reviewer(request,proposedreviewerId):
    context = RequestContext(request)
    user = request.user
    prop_rev = ProposedReviewer.objects.get( pk = proposedreviewerId )
    project = Project.objects.get(pk = prop_rev.project.pk)

    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')
        if 'delete' in request.POST:
             prop_rev.delete()
             return HttpResponseRedirect(redirect)
        else:
            r = ExcludedReviewerForm(request.POST, instance = prop_rev)

            if r.is_valid():
                r.save()

                return HttpResponseRedirect(redirect)

    else:
        r = ExcludedReviewerForm(instance= prop_rev)

    return render_to_response('rfp/edit_excluded_reviewer.html', {'f' : r, 'project' : project, 'user' : user, 'prop_rev' : prop_rev},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def add_unique_reviewer(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)

    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')
        r = ProposedReviewerForm(request.POST)
        if r.is_valid():
            reviewer = r.save(commit = False)
            reviewer.project = project
            reviewer.type = 'proposed'
            reviewer.save()

            return HttpResponseRedirect(redirect)
    else:
        r = ProposedReviewerForm()

    return render_to_response('rfp/add_unique_review.html', {'f' : r, 'project' : project, 'user' : user},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def exclude_unique_reviewer(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)

    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')

        r = ExcludedReviewerForm(request.POST)
        if r.is_valid():
            reviewer = r.save(commit = False)
            reviewer.project = project
            reviewer.type = 'excluded'
            reviewer.email = ''
            reviewer.save()

            return HttpResponseRedirect(redirect)
    else:
        r = ExcludedReviewerForm()

    return render_to_response('rfp/exclude_unique_review.html', {'f' : r, 'project' : project, 'user' : user},context)

#Make it DRY
def redirect_add_form(request,project,form_1,form_2):

    alldata = request.POST
    redirect = alldata.get('redirect','0')
    if redirect:
                    redirect_url = reverse('create_project_budget', args = [project.pk])
                    return redirect_url
    else:
                    redirect_url = reverse('project_budget', args = [project.pk])
                    return redirect_url

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def add_budget_hr(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)

    if request.method == 'POST':
        form = BudgetLineHR(request.POST)
        alldata = request.POST
        redirect = alldata.get('redirect','0')

        if form.is_valid() :

                bl = form.save(commit=False)
                bl.project = project
                bl.category = 'HR'
                bl.save()

                print(redirect)

                return HttpResponseRedirect(redirect)

    else:
        form = BudgetLineHR()

    return render_to_response('rfp/add_budget_hr.html',{'form' : form, 'user' : user, 'project' : project},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def edit_budget_hr(request, budgetlineId):
    context = RequestContext(request)
    user = request.user
    bl = BudgetLine.objects.get(id = budgetlineId )
    project_id = bl.project.pk


    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')

        if 'delete' in request.POST:
             bl.delete()
             return HttpResponseRedirect(redirect)

        else:
            form = BudgetLineHR(request.POST,instance=bl)

            if form.is_valid():
              form.save()
              return HttpResponseRedirect(redirect)

    else:
        form = BudgetLineHR(instance=bl)

    return render_to_response('rfp/edit_budget_hr.html',{'form' : form, 'user' : user,'bl': bl},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def add_budget_eq(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)

    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')
        form = BudgetLineEQ(request.POST,request.FILES)

        if form.is_valid():
            bl = form.save(commit=False)
            bl.project = project
            bl.category = 'EQ'
            bl.save()

            return HttpResponseRedirect(redirect)

    else:
        form = BudgetLineEQ()

    return render_to_response('rfp/add_budget_eq.html',{'form' : form, 'user' : user, 'project' : project},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def edit_budget_eq(request, budgetlineId):
    context = RequestContext(request)
    user = request.user
    bl = BudgetLine.objects.get(id = budgetlineId )
    project_id = bl.project.pk

    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')

        if 'delete' in request.POST:
             bl.delete()
             return HttpResponseRedirect(redirect)

        else:
            form = BudgetLineEQ(request.POST,request.FILES,instance=bl)

            if form.is_valid():
                form.save()

                return HttpResponseRedirect(redirect)

    else:
        form = BudgetLineEQ(instance=bl)

    return render_to_response('rfp/edit_budget_eq.html',{'form' : form, 'user' : user,'bl': bl},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def add_budget_op(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)
    alldata = request.POST
    redirect = alldata.get('redirect','0')

    if request.method == 'POST':

        form = BudgetLineOP(request.POST)

        if form.is_valid() :
            bl = form.save(commit=False)
            bl.project = project
            bl.category = 'OC'
            bl.save()

            return HttpResponseRedirect(redirect)

    else:
        form = BudgetLineOP()

    return render_to_response('rfp/add_budget_op.html',{'form' : form, 'user' : user, 'project' : project},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def edit_budget_op(request, budgetlineId):
    context = RequestContext(request)
    user = request.user
    bl = BudgetLine.objects.get(id = budgetlineId )
    project_id = bl.project.pk

    if request.method == 'POST':
        alldata = request.POST
        redirect = alldata.get('redirect','0')

        if 'delete' in request.POST:
             bl.delete()
             return HttpResponseRedirect(redirect)

        else:
            form = BudgetLineOP(request.POST,instance=bl)

            if form.is_valid() :
                form.save()

                return HttpResponseRedirect(redirect)

    else:
        form = BudgetLineOP(instance=bl)

    return render_to_response('rfp/edit_budget_op.html',{'form' : form, 'user' : user,'bl': bl},context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
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

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def prop_reviewer_list(request,projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get( pk = projectId )

    prop_rev_list = ProposedReviewer.objects.filter(project = project)

    return render_to_response('rfp/list_of_proposed_reviewer.html', {'user' : user, 'project' : project, 'proposed_reviewers' : prop_rev_list}, context)

@user_passes_test(is_reviewer,login_url='/login/',redirect_field_name='next')
def post_review(request,reviewId):
    context = RequestContext(request)
    user = request.user
    user_profile = UserProfile.objects.get(user = user.pk)
    review = Review.objects.get(pk = reviewId, user=user.pk)
    project = Project.objects.get(pk = review.project.pk)
    rfp = RfpCampaign.objects.get(id = project.rfp.id)
    questions = rfp.get_questions()
    is_p = is_pi(user)
    is_rev = is_reviewer(user)

    review_item = Review.objects.get(user = user.pk, project = project.pk)
    review_model_dict = model_to_dict(review_item)

    if request.method == 'POST':
        form = ReviewForm(request.POST,request.FILES,questions=questions)

        if form.is_valid():
                    form_data = form.cleaned_data
                    updated_review = Review.objects.update_or_create(user = user.pk, project = project.pk, defaults=form_data)
                    print(updated_review)

                    return HttpResponseRedirect(reverse('project_review', args=[project.pk]))

    else:
        form = ReviewForm(initial= review_model_dict,questions = questions)

    return render_to_response('rfp/post_review.html',{'is_pi' : is_p, 'is_rev': is_rev,
        'form' : form, 'project' : project, 'user' : user, 'up' : user_profile,'review' : review}, context)

@user_passes_test(is_reviewer,login_url='/project/login_no_permission/',redirect_field_name='next')
def post_review_waiver(request,reviewId):
    context = RequestContext(request)
    user = request.user
    review = Review.objects.get(pk = reviewId, user=user.pk)
    project = Project.objects.get(pk = review.project.pk)
    print (request.POST)

    if review.user.pk == user.pk:
        if request.method =='POST':
            if ('no_conflict') in request.POST['optradio'] or ('agreement') in request.POST['optradio']:
                return HttpResponseRedirect(reverse('project_detail', args = [project.pk]))
            elif ('refuse') in request.POST['optradio']:
                return HttpResponseRedirect(reverse('logout'))

    else:
        return HttpResponseRedirect(reverse('login'))


    context_dict = {'review' : review, 'project' : project}

    return render_to_response('rfp/post_review_waiver.html', context_dict, context)


@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def rfp_campaign(request,rfpcampaignId):
    context = RequestContext(request)
    user = request.user
    rfp_campaign=RfpCampaign.objects.get(id=rfpcampaignId)

    context_dict = {'user':user,'rfp_campaign':rfp_campaign}

    return render_to_response('rfp/rfp_details.html',context_dict,context)

@user_passes_test(is_pi,login_url='/project/login_no_permission/',redirect_field_name='next')
def list_of_call_for_proposal(request):
    context= RequestContext(request)

    rfp_c = RfpCampaign.objects.all()

    context_dict = {'rfp_c' : rfp_c}

    return render_to_response('rfp/rfp_list.html',context_dict,context)





def test (request):
    from django.template.loader import render_to_string
    from django.core.mail import send_mail
    context= RequestContext(request)
    user = request.user
    from urlcrypt import lib as urlcrypt
    token = urlcrypt.generate_login_token(user, reverse('user_profile'))
    encoded_url = reverse('urlcrypt_redirect', args=(token,))

    c = {'user' : user, 'url' : encoded_url}
    msg_plain = render_to_string('rfp/email/invitation_link.txt',c)
    msg_html = render_to_string('rfp/email/invitation_link.html',c)

    send_mail('Your project has been succesfully submitted',
    msg_plain, 'contact@icfrc.fr', ['sgug@outlook.com'],
    html_message=msg_html, fail_silently=False)

    print('Email Sent ?')

    context_dict = {'user' : user, 'url' : encoded_url}

    return render_to_response('rfp/test.html',context_dict,context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard(request):
    context = RequestContext(request)
    user = request.user

    list_of_projects = Project.objects.all()
    list_of_review = Review.objects.all()

    context_dict = {'list_of_projects' : list_of_projects, 'list_of_review': list_of_review, 'user': user }

    return render_to_response('dashboard.html', context_dict, context)

