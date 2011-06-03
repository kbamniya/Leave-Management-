from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
import random
from django.contrib.sites.models import Site
from django.conf import settings
from django.template import Context
from django.db.models.signals import class_prepared


# Create your models here.


class UserProfile(models.Model):
    user             = models.ForeignKey(User)
    role_of_user     = models.CharField(max_length=200)
    join_date        = models.DateTimeField(blank=True, null=True)
     


    

    

LEAVE_TYPE_CHOICES = ( ('HD','Half Day'),('FD','Full Day'))
LEAVE_REFER_CHOICES = ( ('YL','Your Leave'),('RL','Refer Leave'))
class Leave(models.Model):
    
    
    leave_refer      = models.CharField(max_length=2, choices=LEAVE_REFER_CHOICES)
    
    refer            = models.ForeignKey(UserProfile, related_name = "refer")
    leave_type       = models.CharField(max_length=2, choices=LEAVE_TYPE_CHOICES)
    email            = models.EmailField(null = True, blank = True)
    leave_subject    = models.CharField(max_length=40)
    leave_reason     = models.TextField(max_length=200)
    leave_start_date = models.DateTimeField(blank=True, null=True)
    leave_end_date   = models.DateTimeField(blank=True, null=True)
    leave_status     = models.CharField(max_length=20)

##    def __unicode__(self):
##        return self.email 
##
##    def save(self, *args, **kwargs):
##        htmly     = get_template('inviteTemplate.html')
##        name =self.email.split("@", 1)[0];
##        location = "All" 
##        confirmString = str(random.randint(0,1000000))
##        current_site = Site.objects.get(id=settings.SITE_ID)
##
##        self.confirmString = confirmString        
##        emailData = Context({ 'name': name ,'confirmString':confirmString,'location':location, 'domain':current_site.domain, 'from':current_site.name})
##
##        html_content = htmly.render(emailData)
##        msg = EmailMultiAlternatives("Leave","", 'Leave_Management_System\'s Project', [self.email])
##        msg.attach_alternative(html_content, "text/html")
##        try:
##            flag = msg.send()
##            super(Leave, self).save(*args, **kwargs) # Call the "real" save() method.
##        except:     
##            pass
##
##        return flag
##
