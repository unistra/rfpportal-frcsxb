__author__ = 'Sylvestre'
from django.shortcuts import render,render_to_response,HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from user_profile.views import is_pi,is_reviewer


def index(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if is_pi(request.user):
                    HttpResponseRedirect(reverse('rfp_list'))
                if is_reviewer(request.user):
                    HttpResponseRedirect(reverse('user_profile'))
            else:
                # Return a 'disabled account' error message
                HttpResponse('Not an active User!')

    context_dict = {}

    return render_to_response('registration/home_page_login.html',context_dict,context)
