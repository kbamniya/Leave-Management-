from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from LMS.models import Leave, UserProfile
from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import render_to_response

from django.template import Context, loader
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from LMS.form import LeaveForm
from LMS.form import UserProfileForm



#def index(request):
 #   return HttpResponse("Hello, world. You're at the poll index.")
def index(request):
    #latest_option_list = Leave.objects.all().order_by('name')[:5]
    return render_to_response('home.html', {}, context_instance=RequestContext(request))

@login_required
def profile(request):
    #p = get_object_or_404(User, pk=user_id)
    return render_to_response('profile.html', {}, context_instance=RequestContext(request))

#@login_required
def logout(request):
    authLogout(request)
    return render_to_response('login.html')

def userprofileForm (request) :
    userprofileFormObj = UserProfileForm()
    return render_to_response('userprofileForm.html', {'formObj': userprofileFormObj})

def leaveForm (request) :
    leaveFormObj = LeaveForm()
    
    
    return render_to_response('leaveForm.html', {'formObj': leaveFormObj})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LeaveForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            
            
            
            form.save()
            leave_refer = form.cleaned_data['leave_refer']
            refer = form.cleaned_data['refer']
            #leave type = form.cleaned_data['leave type']
            email = form.cleaned_data['email']



            # Process the data in form.cleaned_data
            # ...
            return render_to_response('contact.html', {'form': form,}) # Redirect after POST
    else:
        form = LeaveForm() # An unbound form
        
    return render_to_response('contact.html', {'form': form,})





##
##
#def logout_view(request):
 #       logout(request)
##def my_view(request):
##    if not request.user.is_authenticated():
##        return HttpResponseRedirect('/login/?next=%s' % request.path)
##def my_view(request):
##    if not request.user.is_authenticated():
##        return render_to_response('myapp/login_error.html')
##
##@login_required
##def my_view(request):
##
##
##
##@login_required(redirect_field_name='my_redirect_field')
##def my_view(request):
##
#@login_required(login_url='Leave_Management_System/template/')
#def my_view(request):


