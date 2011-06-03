from django.forms import ModelForm
from django import forms
from LMS.models import UserProfile
from LMS.models import Leave
#from django.forms.extras.widgets import RadioSelect


class UserProfileForm(ModelForm):
    class Meta():
        model = UserProfile

LEAVE_REFER_CHOICES = ( ('YL','Your Leave'),('RL','Refer Leave'))
class LeaveForm(ModelForm):
    leave_refer =forms.CharField (widget=forms.RadioSelect(choices = LEAVE_REFER_CHOICES), label = "Leave Refer")     
    class Meta():
        model = Leave
        exclude = ('leave_status',)
        
