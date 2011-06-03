from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'LMS.views.index', name="index"),
    (r'^(?P<LMS_id>\d+)/$', 'detail'),
                     
    url(r'^userprofileform/$','LMS.views.userprofileForm', name = "userprofileentery"),
    url(r'^leaveform/$','LMS.views.leaveForm', name = "leaveentery"), 
)


