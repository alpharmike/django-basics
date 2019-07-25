from django.contrib import admin
from Application.models import Topic, Webpage, AccessRecord, MyUser, UserProfileInfo

# Register your models here.


admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(MyUser)
admin.site.register(UserProfileInfo)
