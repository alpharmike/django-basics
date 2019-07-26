from django import forms
from django.core import validators
from django.contrib.auth.models import User
from .models import MyUser, UserProfileInfo


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name Needs to Start With Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Verify Your Email: ")
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                  validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        # returning the dictionary containing cleaned data, this method applies initial validations to the inputs
        clean_data = super().clean()
        email = clean_data['email']
        verified_email = clean_data['verify_email']

        if email != verified_email:
            raise forms.ValidationError("Emails Do Not Match!")


class SignUpForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'
        # widgets = {
        #     "first_name": forms.TextInput(attrs={'placeholder': 'Enter First Name', 'id': 'First_name'}),
        #     "last_name": forms.TextInput(attrs={'placeholder': 'Enter Last Name', 'id': 'Last_name'}),
        # }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
