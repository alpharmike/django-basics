from django.urls import path
from . import views

'''
actually it's wrong to do this, because we have to create another application by calling
django-admin startapp app_name, and creating another urls.py module for it
'''

app_name = 'extras'

urlpatterns = [
    path('', views.show_extra, name='extra')
]
