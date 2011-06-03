

from LMS.models import UserProfile
from LMS.models import Leave
from django.contrib import admin
#from option.models import Person
from django.contrib.auth.models import User



admin.site.register(Leave)
#admin.site.register(User)






admin.site.register(UserProfile)


