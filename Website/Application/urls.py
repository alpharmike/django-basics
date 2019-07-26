from django.urls import path
from . import views

app_name = 'relatives'

urlpatterns = [
    path('', views.show_app, name='app'),
    path('rel/', views.show_rel, name="rel"),
    path('login/', views.user_login, name="login"),
    path('', views.UserDetailView.as_view(), name='user_detail')
]
