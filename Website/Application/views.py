from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Topic, Webpage, AccessRecord, MyUser, UserProfileInfo  # or from Application.models
from django.forms import modelform_factory
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    # users_list = User.objects.order_by('last_name')
    date_dict = {'access_records': webpages_list}
    # user_dict = {'user_records': users_list}
    # my_dict = {'insert_me': "hello"}
    return render(request, 'index.html', context=date_dict)


def show_users(request):
    users_list = MyUser.objects.order_by('last_name')
    user_dict = {'user_records': users_list}
    return render(request, 'user.html', context=user_dict)


def form_name_view(request):
    form = forms.FormName()

    if request.method == "POST":
        form = forms.FormName(request.POST)

        if form.is_valid():
            form.save()
            print("Name: " + form.cleaned_data['name'])
            print("Email: " + form.cleaned_data['email'])
            print("Text: " + form.cleaned_data['text'])

    return render(request, 'form_page.html', {'form': form})


def sign_up(request):
    # form = modelform_factory(User, fields=('first_name', 'last_name', 'email'))
    form = forms.SignUpForm()
    if request.method == "POST":
        form = forms.SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            print("First Name: " + form.cleaned_data['first_name'])
            print("Last Name: " + form.cleaned_data['last_name'])
            print("Email: " + form.cleaned_data['email'])
            return index(request)

    return render(request, 'sign_up.html', {'form': form})


# working with relative templates

def show_rel(request):
    return render(request, 'relative.html')


def show_app(request):
    return render(request, 'app.html')


def show_extra(request):
    context = {'text': 'Hello World', 'number': 100, 'text_cut': 'Cut Text'}
    return render(request, 'extra.html', context=context)


def register(request):
    # user_form = forms.UserForm()
    # profile_form = forms.ProfileForm()
    registered = False
    if request.method == "POST":
        user_form = forms.UserForm(data=request.POST)
        profile_form = forms.ProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=True)  # the save method returns an instance of User object
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = forms.UserForm()
        profile_form = forms.ProfileForm()

    context = {'registered': registered, 'user_form': user_form, 'profile_form': profile_form}
    return render(request, 'registration.html', context=context)


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")

        else:
            return HttpResponse("Username and Password Do Not Match!")
    else:
        return render(request, 'login.html')


@login_required  # only if the user has logged in, he can log out
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
