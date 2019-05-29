from django import forms
from django.core import validators
from first_app.models import UserProfileInfo
from django.contrib.auth.models import User

#this function will help if you want to make validation function on your own
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("need to start with z")


class formName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label='type email again')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput,
                                 validators = [validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        another = all_clean_data['verify_email']

        if email != another:
            raise forms.ValidationError("both email must be same")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site','portfolio_pic')
