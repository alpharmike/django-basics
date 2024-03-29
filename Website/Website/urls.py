"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Application import views

urlpatterns = [
    path('', views.index, name="index"),
    path('app/', include('Application.urls')),
    path('extra/', include('Application.extraurls')),
    path('users/', views.show_users, name="user"),
    path('forms/', views.form_name_view, name="form"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('register/', views.register, name="register"),
    path('logout/', views.user_logout, name="logout"),
    # path('', views.CBView.as_view(), name='index'),
    path('/user_list', views.UserListView.as_view(), name='user_list'),
    path('(?P<slug>[-\w]+)', views.UserDetailView.as_view(), include('Application.urls', namespace='relatives')),
    path('admin/', admin.site.urls),
]
