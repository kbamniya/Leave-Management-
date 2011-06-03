from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib import admin
from django.contrib.auth import views as auth_views
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^Leave_Management_System/', include('Leave_Management_System.foo.urls')),
    url(r'^LMS/', include('LMS.urls')),
    (r'^accounts/profile/$', 'LMS.views.profile'),
    (r'^contact/$','LMS.views.contact' ), 
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'loginPage.html'}, name="auth_login"),                   
    url(r'^accounts/logout/$', auth_views.logout,{'template_name': 'logout.html'}, name = "auth_logout"),



    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^admin/(.*)', admin.site.root),
    #(r'^LMS/', include('registration.urls')),
    #(r'^$', direct_to_template,{ 'template': 'home.html' }, 'index'),
    )

