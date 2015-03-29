from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,Group,Permission
from django.contrib.auth import authenticate, login
from forms import sign_up
from models import UserProfile
from rfp.models import Project,Review,RequestForProposal,RfpCampaign

# Create your views here.

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

            if pi:
                pi_group = Group.objects.get(name='Principal_Investigator')
                user.group_id = pi_group.id

            if reviewer:
                rev_group = Group.objects.get(name='Reviewer')
                user.group_id = rev_group.id

            user.save()

            user_profile = UserProfile.objects.get(user_id=user.id)
            user_profile.last_name = form.cleaned_data['last_name']
            user_profile.first_name = form.cleaned_data['first_name']
            user_profile.address = form.cleaned_data['address']
            user_profile.zip = form.cleaned_data['zip']
            user_profile.city = form.cleaned_data['city']



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


@login_required(login_url='/login/')
def index_profile(request):

    context = RequestContext(request)
    user = request.user

    user_account = UserProfile.objects.get(user = user.id)

    projects = Project.objects.filter(user = user.id)
    reviews = Review.objects.filter(user = user.id)

    context_dict = {'user_profile': user_account,'projects' : projects,'reviews': reviews}

    return render_to_response('user_profile/profile.html',context_dict,context)

