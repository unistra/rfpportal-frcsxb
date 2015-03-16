from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from forms import sign_up

# Create your views here.

def create_profile(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = sign_up(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username, email, form.cleaned_data['password'])
            user.save()


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

    return render_to_response('user_profile/profile.html',context)