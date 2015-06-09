from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate, login
from forms import sign_up,UserUpdate
from models import UserProfile
from django.core.urlresolvers import reverse

from rfp.models import Project,Review,RfpCampaign

# Create your views here.
def is_reviewer(User):
    return User.groups.filter(name='Reviewer').exists()

def is_pi(User):
    return User.groups.filter(name = 'Principal_Investigator').exists()

#Create a new profile
def create_profile(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = sign_up(request.POST)

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
        form = sign_up()

    return render_to_response('user_profile/create_profile.html',{'form':form},context)

#Edit an existing profile
@login_required(login_url="/login/?next={% 'user_profile' %}")
def edit_profile(request):
    context = RequestContext(request)
    user = request.user
    up = UserProfile.objects.get(user = user.id)

    if request.method == 'POST':
        form = UserUpdate(request.POST,instance = up)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('../profile/')

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

    user_account = UserProfile.objects.get(user = user.id)
    projects = Project.objects.filter(user = user.id).order_by('-starting_date')
    reviews = Review.objects.filter(user=user.pk)


    context_dict = {'user_profile': user_account,'projects' : projects, 'reviews' : reviews, 'is_pi' : is_pi, 'is_rev' : is_rev}

    return render_to_response('user_profile/profile.html',context_dict,context)

@login_required(login_url="/")
def post_homepage_login_landing_page(request):
    context = RequestContext(request)
    user=request.user

    is_pi = user.groups.filter(name = 'Principal_Investigator').exists()
    is_rev = user.groups.filter(name = 'Reviewer').exists()
    rfp_c = RfpCampaign.objects.all()
    projects = Project.objects.filter(user = user).order_by('-id')[:3]

    reviews = Review.objects.filter(user=user.pk)

    context_dict = {'reviews' : reviews, 'is_pi' : is_pi, 'is_rev' : is_rev, 'rfp_c' : rfp_c, 'projects':projects}

    return render_to_response('user_profile/post_homepage_login_landing_page.html',context_dict,context)

