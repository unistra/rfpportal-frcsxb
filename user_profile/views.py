from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate, login

from forms import UserDetails,UserUpdate,RfpCreate,SearchForm,CreateUser

from models import UserProfile
from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict

from rfp.forms import ProposedReviewerForm,ProjectForm,DashboardEditForm,BudgetLineHR,BudgetLineEQ,BudgetLineOP
from rfp.models import Project,Review,RfpCampaign,BudgetLine,ProposedReviewer,Tag
from rfp.views import store_redirect_url,get_redirect_url,budget_line_sum

# Create your views here.
def is_reviewer(User):
    return User.groups.filter(name='Reviewer').exists()

def is_pi(User):
    return User.groups.filter(name = 'Principal_Investigator').exists()

def is_staff(User):
    return User.is_staff

def is_staff_or_sb(User):
    return User.is_staff or User.groups.filter(name = 'Scientific_board').exists()

def status_choices(model):
    """
    Return a dict. with all status choices of the related model.
    :param model: Object
    :return: Dict
    """

    l = list()
    for r in model.STATUS_CHOICES:
                l.append(r[0])
    return l

#Create a new profile
def create_profile(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = UserDetails(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            pi = form.cleaned_data['is_pi']
            reviewer = form.cleaned_data['is_pi']
            user = User.objects.create_user(username, email, form.cleaned_data['password'])

            user.last_name = form.cleaned_data['last_name']
            user.first_name = form.cleaned_data['first_name']
            user.save()

            if pi:
                pi_group = Group.objects.get(name='Principal_Investigator')
                user.groups.add(pi_group)


            if reviewer:
                rev_group = Group.objects.get(name='Reviewer')
                user.groups.add(rev_group)


            user_profile = UserProfile.objects.get(user_id=user.id)
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.organization = form.cleaned_data['organization']
            user_profile.address = form.cleaned_data['address']
            user_profile.zip = form.cleaned_data['zip']
            user_profile.city = form.cleaned_data['city']
            user_profile.num_connection = 1

            user_profile.save()

            user_logged_in = authenticate(username=username, password=form.cleaned_data['password'])

            if user_logged_in is not None:
                    # the password verified for the user
                    if user_logged_in.is_active:
                        login(request, user_logged_in)
                        return HttpResponseRedirect('../profile/')
                    else:
                        return HttpResponse("The password is valid, but the account has been disabled!")
            else:
                    # the authentication system was unable to verify the username and password
                    return HttpResponse("The username and password were incorrect.")

        return HttpResponse('User Created ?')

    else:
        form = UserDetails()

    return render_to_response('user_profile/create_profile.html',{'form':form},context)

#Edit an existing profile
@login_required(login_url="/login/?next={% 'user_profile' %}")
def edit_profile(request):
    context = RequestContext(request)
    user = request.user
    up = UserProfile.objects.get(user = user.id)
    redirect = get_redirect_url(request)
    if request.method == 'POST':
        form = UserUpdate(request.POST,instance = up)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect)

    else:
        form = UserUpdate(instance = up)

    context_dict = {'user' : user, 'form' : form, 'UP' : up}
    return render_to_response('user_profile/edit_profile.html', context_dict, context)

#Access an existing profile
@login_required(login_url="/login/?next={% 'user_profile' %}")
def index_profile(request):

    context = RequestContext(request)
    user = request.user

    is_pi = user.groups.filter(name = 'Principal_Investigator').exists()
    is_rev = user.groups.filter(name = 'Reviewer').exists()
    store_redirect_url(request)

    user_account = UserProfile.objects.get(user = user.id)
    projects = Project.objects.filter(user = user.id).order_by('-starting_date')
    reviews = Review.objects.filter(user=user.pk)

    context_dict = {'user_profile': user_account,'projects' : projects, 'reviews' : reviews, 'is_pi' : is_pi, 'is_rev' : is_rev}

    return render_to_response('user_profile/profile.html',context_dict,context)

import datetime
@login_required(login_url="/")
def post_homepage_login_landing_page(request):
    context = RequestContext(request)
    user=request.user

    if user.is_staff:
        return redirect(reverse('dashboard'))

    is_pi = user.groups.filter(name = 'Principal_Investigator').exists()
    is_rev = user.groups.filter(name = 'Reviewer').exists()
    rfp_c = RfpCampaign.objects.filter(status = 'open')
    projects = Project.objects.filter(user = user).order_by('-id')[:3]

    list_of_rfp = RfpCampaign.objects.exclude(status='closed').exclude(status='under_review').exclude(deadline__lt = datetime.datetime.now())

    list_of_cs_rfp = RfpCampaign.objects.exclude(status='closed')

    project_list = Project.objects.filter(rfp__in = list(list_of_cs_rfp))
    list_of_tagged_project = Tag.objects.filter(user= user).filter(project__in = list(project_list))



    store_redirect_url(request)

    widget = True

    reviews = Review.objects.filter(user=user.pk)

    context_dict = {'list_of_tagged_project': list_of_tagged_project, 'list_of_rfp' : list_of_rfp,'list_of_cs_rfp' : list_of_cs_rfp, 'widget' : widget, 'reviews' : reviews, 'is_pi' : is_pi, 'is_rev' : is_rev, 'rfp_c' : rfp_c, 'projects':projects}

    return render_to_response('user_profile/post_homepage_login_landing_page.html',context_dict,context)

#Dashboard_Admin_Views
@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard(request):
    context = RequestContext(request)
    user = request.user

    list_of_projects = Project.objects.all()
    list_of_review = Review.objects.all()
    list_of_rfp = RfpCampaign.objects.exclude(status = 'closed')

    context_dict = {'list_of_projects' : list_of_projects, 'list_of_review': list_of_review, 'user': user, 'list_of_rfp' : list_of_rfp}

    return render_to_response('dashboard/dashboard.html', context_dict, context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_create_rfp(request):
    context = RequestContext(request)
    user = request.user

    if request.method == "POST":
        form = RfpCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard_rfp_listing'))

    else:
        form = RfpCreate()

    context_dict = {'form' : form, 'user' : user}

    return render_to_response('dashboard/dashboard_create_rfp.html', context_dict, context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_edit_rfp(request, rfpId):
    context = RequestContext(request)
    user = request.user
    rfp = RfpCampaign.objects.get(id = rfpId)

    if request.method == "POST":
        form = RfpCreate(request.POST,request.FILES,instance=rfp)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard_rfp_listing'))

    else:
        form = RfpCreate(instance = rfp)

    context_dict = {'form' : form, 'user' : user, 'rfp' : rfp}

    return render_to_response('dashboard/dashboard_edit_rfp.html', context_dict, context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_rfp_listing(request):
    context = RequestContext(request)
    user = request.user
    rfp_list = RfpCampaign.objects.all().order_by('-year')

    context_dict = {'rfp_list' : rfp_list, 'user' : user}

    return render_to_response('dashboard/dashboard_rfp_listing.html', context_dict, context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_rfp_details(request,rfpId):
    context = RequestContext(request)
    user = request.user
    rfp = RfpCampaign.objects.get(id = rfpId)
    project_list = Project.objects.filter(rfp = rfp.id)
    review_status = status_choices(Review)

    context_dict = {'rfp' : rfp, 'user' : user, 'project_list':project_list, 'review_status':review_status}

    return render_to_response('dashboard/dashboard_rfp_details.html', context_dict, context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_project_details(request,projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)
    project_data = ProjectForm(data=model_to_dict(project), questions = project.rfp.get_project_questions())
    store_redirect_url(request)

    budget_line_list = BudgetLine.objects.filter(project = project)
    hr_budget_line_list = BudgetLine.objects.filter(project = project,category = 'HR')
    oc_budget_line_list = BudgetLine.objects.filter(project = project,category = 'OC')
    eq_budget_line_list = BudgetLine.objects.filter(project = project,category = 'EQ')

    oc_total = budget_line_sum(oc_budget_line_list)
    hr_total = budget_line_sum(hr_budget_line_list)
    eq_total = budget_line_sum(eq_budget_line_list)

    prop_rev_list = ProposedReviewer.objects.filter(project = project).exclude(type='USER_EXCLUDED')
    excluded_rev_list = ProposedReviewer.objects.filter(project = project, type='USER_EXCLUDED')
    total_budgeted = budget_line_sum(budget_line_list)

    review_list = Review.objects.filter(project = project.id)
    tag_list = Tag.objects.filter(project = project)

    context_dict = {'oc_total' : oc_total, 'eq_total' : eq_total, 'hr_total' : hr_total, 'tag_list' : tag_list, 'project':project,'project_data' : project_data,
                    'budget_line_list': budget_line_list,
                    'total' : total_budgeted,'hr_budget_lines_list' : hr_budget_line_list, 'oc_budget_lines_list' : oc_budget_line_list,
                    'eq_budget_lines_list' : eq_budget_line_list,'excluded_rev_list' : excluded_rev_list,'prop_rev_list' : prop_rev_list, 'list_of_review' : review_list}

    return render_to_response('dashboard/dashboard_project_details.html', context_dict, context)

def search_form(request,queryset,Model):
    if request.method =="POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            search = str(form.cleaned_data['search']).lower()
            results = list()
            #Loop over object in queryset of model
            for object in queryset:
                model_dict = model_to_dict(object)
                print (model_dict)

                #Check if the searched string is included in one of the Object field
                """
                for key in model_dict:
                    print('Searching: ')
                    print (model_dict[key])
                """

                if search in str(model_dict['name']):
                        #Add the users id in a list
                        print('I found d')
                        results.append(object.id)
                        break
            #Re-initialize the model queryset filtering by found objects.id
            queryset = Model.objects.filter(pk__in = (results))


    else:
        form = SearchForm()
        queryset = Model.objects.all()

    return queryset

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_project_list(request):
    context = RequestContext(request)
    user = request.user
    project_list = Project.objects.all().order_by('status')
    form = SearchForm()

    search_form(request,project_list,Project)

    context_dict = {'project_list' : project_list,'form':form}

    return render_to_response('dashboard/dashboard_project_list.html', context_dict, context)

def get_user_from_group(group):
    gr = Group.objects.get(name=group)
    if gr:
        return gr.user_set.all()
    else:
        return HttpResponse('User Group does not exists')

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_reviewers_list(request):
    context = RequestContext(request)
    user = request.user
    group = Group.objects.get(name='Reviewer')
    redirect = store_redirect_url(request)

    """
    if request.method =="POST":
        form = SearchForm(request.POST)

        if form.is_valid():
            search = str(form.cleaned_data['search']).lower()

            #Initialization of lists
            reviewers_list = group.user_set.all()
            users_id = list()

            #Loop over users in reviewers group member
            for u in reviewers_list:
                print u
                model_dict = model_to_dict(u)
                print model_dict

                #Check if the searched string is included in one of the User field
                for key in model_dict:
                    if search in str(model_dict[key]).lower():
                        #Add the users id in a list
                        users_id.append(u.id)
                        break
            #Re-initialize the lists of reviewers including only the users with id found in the loop
            reviewers_list = group.user_set.filter(pk__in = (users_id))

    else:
        form = SearchForm()
        """
    reviewers_list = group.user_set.all()

    users_id = list()

    context_dict = {'reviewers_list' : reviewers_list, 'users_id' : users_id}

    return render_to_response('dashboard/dashboard_reviewers_list.html', context_dict, context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_reviewer_detail(request, reviewerId):
    context = RequestContext(request)
    user = request.user
    reviewer = User.objects.get(id = reviewerId)
    reviewer_dict = model_to_dict(reviewer.userprofile)
    list_of_review = Review.objects.filter(user = reviewer.id)
    #Date of last review
    last_review = Review.objects.filter(user = reviewer.id).order_by('-date')[:1]
    if last_review:
        for r in last_review:
            last_review_date = r.date
    else:
        last_review_date = None

    #Information of Reviewer presented in the UserUpdate form
    reviewer_information = UserUpdate(reviewer_dict)

    #Total number of review made by reviewer
    num_of_review = Review.objects.filter(user = reviewer.id, status = 'completed').count()

    context_dict = {'reviewer' : reviewer,'user' : user, 'list_of_review' : list_of_review,'reviewer_information':reviewer_information,'num_of_review' : num_of_review,
                    'last_review_date' : last_review_date}

    return render_to_response('dashboard/dashboard_reviewer_detail.html',context_dict,context)

@user_passes_test(is_staff_or_sb,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_add_admin_proposed_reviewer(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(pk = projectId)
    redirect = get_redirect_url(request)
    print(redirect)

    if request.method == 'POST':

        r = ProposedReviewerForm(request.POST)
        if r.is_valid():
            reviewer = r.save(commit = False)
            reviewer.project = project
            if 'dashboard' in redirect:
                reviewer.type = 'ADMIN_PROPOSED'

            if 'scib' in redirect:
                reviewer.type = 'BOARD_PROPOSED'

            else:
                reviewer.type = 'USER_PROPOSED'
            reviewer.save()
            if 'scib' in redirect:
                return HttpResponseRedirect(str(reverse('scientific_board_project_details', args=(project.id,))) + '?a=#reviewer')
            else:
                return HttpResponseRedirect(redirect)
    else:
        r = ProposedReviewerForm()

    return render_to_response('dashboard/dashboard_add_reviewer.html', {'f' : r, 'project' : project, 'user' : user},context)

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_review_list(request):
    context = RequestContext(request)
    user = request.user
    list_of_review = Review.objects.all().order_by('-date')
    form = SearchForm()

    context_dict = {'list_of_review' : list_of_review, 'user' : user, 'form' : form}

    return render_to_response('dashboard/dashboard_review_list.html',context_dict,context)

from django.core.mail import send_mail
@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_invite_reviewer(request,propRId):
    context = RequestContext(request)
    user = request.user
    prop_rev = ProposedReviewer.objects.get(id = propRId)

    print(prop_rev.project)

    project = Project.objects.get(id = prop_rev.project.pk)

    prop_rev.invite_reviewer()

    prop_rev.invited = True
    prop_rev.save()

    return HttpResponseRedirect(reverse('dashboard_project_details', args = [project.id]))

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_follow_up_with_reviewer(request,reviewId):
    context = RequestContext(request)
    user = request.user

    review = Review.objects.get(id = reviewId)
    project = Project.objects.get(id = review.project.id)

    if review.status == 'pending':
        review.send_invitation_email_to_reviewer()

    elif review.status == 'accepted':
        review.send_follow_up_invitation_email_to_reviewer()

    return HttpResponseRedirect(reverse('dashboard_project_details', args = [project.id]))

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_send_results(request,projectId):
    project = Project.objects.get(id = projectId)
    project.send_results_email()

    return HttpResponseRedirect(reverse('dashboard_rfp_details', kwargs={'rfpId' : project.rfp.id}))

@user_passes_test(is_staff,login_url='/project/login_no_permission/',redirect_field_name='next')
def dashboard_pi_list(request):
    context = RequestContext(request)
    user = request.user
    group = Group.objects.get(name='Principal_Investigator')
    user_list = group.user_set.all()
    store_redirect_url(request)

    context_dict = {'user_list' : user_list}

    return  render_to_response('dashboard/dashboard_pi_list.html',context_dict,context)

def dashboard_pi_details(request, userId):
    context = RequestContext(request)
    user = request.user
    pi = User.objects.get(id = userId)
    pi_dict = model_to_dict(pi.userprofile)

    project_list = Project.objects.filter(user = pi).order_by('-rfp__year')
    num_project = project_list.exclude(status='draft').count()
    num_proj_granted = project_list.filter(status='granted').count()
    last_granted = project_list.filter(status='granted').first()
    store_redirect_url(request)

    #Information of Reviewer presented in the UserUpdate form
    pi_data = UserUpdate(pi_dict)

    context_dict = {'pi' : pi, 'pi_data' : pi_data, 'project_list' : project_list, 'num_project':num_project,'num_proj_granted': num_proj_granted,'last_granted' : last_granted}

    return  render_to_response('dashboard/dashboard_pi_details.html',context_dict,context)

def dashboard_pi_create(request):
    context = RequestContext(request)

    if request.method == "POST":
        form = CreateUser(request.POST)

        if form.is_valid():
            form.clean_username()
            form.clean()
            new_user = form.save()
            new_user.save()

            g = Group.objects.get(name='Principal_Investigator')
            print(g)
            g.user_set.add(new_user)

            return HttpResponseRedirect(reverse('dashboard_pi_details', args=[new_user.id]))
    else:
        form = CreateUser()

    context_dict = {'form' : form}
    return  render_to_response('dashboard/dashboard_pi_create.html',context_dict,context)


def dashboard_project_edit(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(id = projectId)
    redirect = get_redirect_url(request)


    if request.method == "POST":
        form = DashboardEditForm(request.POST,instance=project)

        if form.is_valid():
            p = form.save()
            return HttpResponseRedirect(redirect)

    else:
        form = DashboardEditForm(instance=project)

    context_dict = {'project' : project, 'form' : form }

    return  render_to_response('dashboard/dashboard_project_edit.html',context_dict,context)

def reset_pwd(request, UserId):
    context = RequestContext(request)
    user = User.objects.get(id = UserId)
    redirect = get_redirect_url(request)

    userprofile = UserProfile.objects.get(user = user)

    userprofile.ResetPwd(request)

    return HttpResponseRedirect(redirect)

def dashboard_edit_profile(request,userId):
    context = RequestContext(request)
    user = User.objects.get(id = userId)
    up = UserProfile.objects.get(user = user.id)
    redirect = get_redirect_url(request)

    if request.method == 'POST':
        form = UserUpdate(request.POST,instance = up)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect)

    else:
        form = UserUpdate(instance = up)

    context_dict = {'user' : user, 'form' : form, 'UP' : up}
    return render_to_response('user_profile/edit_profile.html', context_dict, context)

def scientific_board_project_details(request, projectId):
    context = RequestContext(request)
    user = request.user
    project = Project.objects.get(id = projectId)
    project_data = ProjectForm(data=model_to_dict(project), questions = project.rfp.get_project_questions())
    tag_list = Tag.objects.filter(project=project)

    try:
        user_is_tag = Tag.objects.get(project = project, user = user)
        user_is_tagged = True
    except Tag.DoesNotExist:
        user_is_tagged = False
    except Tag.MultipleObjectsReturned:
        user_is_tagged = True

    store_redirect_url(request)

    list_of_review = Review.objects.filter(project = project, status='completed')
    list_of_bl = BudgetLine.objects.filter(project = project)

    HR_form = BudgetLineHR()
    EQ_form = BudgetLineEQ()
    OC_form = BudgetLineOP()
    prop_rev_list = ProposedReviewer.objects.filter(project = project).exclude(type='USER_EXCLUDED')

    context_dict = {'user_is_tagged' : user_is_tagged,
                    'tag_list' : tag_list, 'prop_rev_list' : prop_rev_list,
                    'project' : project, 'project_data' : project_data, 'list_of_review' : list_of_review,
                    'list_of_bl' : list_of_bl, 'HR_form' : HR_form,'EQ_form': EQ_form, 'OC_form' : OC_form}

    return  render_to_response('user_profile/scientific_board/scientific_board_project_details.html',context_dict,context)

def scientific_board_project_archives(request):
    context = RequestContext(request)
    user = request.user
    project_listing = Project.objects.all()

    context_dict = {'project_listing' : project_listing}

    return render_to_response('user_profile/scientific_board/scientific_board_project_archives.html', context_dict, context)

def add_tag(request,projectId):

    project = Project.objects.get(id = projectId)
    user = request.user

    tag = Tag(project = project, user = user)
    tag.save()

    return HttpResponseRedirect(reverse('scientific_board_project_details', args = [project.id]))

def remove_tag(request,projectId):

    project = Project.objects.get(id = projectId)
    user = request.user

    tag = Tag.objects.filter(project = project, user = user)

    for t in tag:
        t.delete()

    return HttpResponseRedirect(reverse('scientific_board_project_details', args = [project.id]))

from django.contrib.auth.signals import user_logged_in

from django.dispatch import receiver

@receiver(user_logged_in)
def redirect_admin_after_login(user, **kwargs):
    print('Logged_in signal received. User is: ')
    print(user.is_staff)

    if user.is_staff:
        print('Let redirect to Admin')
        return redirect(reverse('dashboard'))
