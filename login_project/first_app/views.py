from django.shortcuts import render
from first_app.models import Topic, Webpage, AccessRecord
from . import forms
from first_app.forms import UserProfileInfoForm, UserForm

#this is for login
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

#this is for class based view
from django.views.generic import View, TemplateView



# Create your views here.
def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'records':webpages_list}

    return render(request, 'first_app/index.html', context=date_dict)

def form_name_view(request):
    form = forms.formName()

    if request.method == 'POST':
        form = forms.formName(request.POST)

        if form.is_valid():
            # code for validate
            print("validation success")

            print("name: " + form.cleaned_data['name'])
            print("email: " + form.cleaned_data['email'])
            print("text: " + form.cleaned_data['text'])

    form_dict = {'form':form}
    return render(request, 'first_app/form_page.html', context=form_dict)

def lvl4index(request):
    dict = {'text':"hello world!", 'number':100}
    return render(request, 'first_app/lvl4index.html', dict)

def other(request):
    return render(request, 'first_app/other.html')

def relative(request):
    return render(request, 'first_app/relative_url.html')

def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            #to prevent from collision commit=false
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'first_app/register.html',
                    {'user_form':user_form,
                    'profile_form':profile_form,
                    'registered':registered }
                  )


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('first_app:lvl4index'))
        else:
            print('someone tried to login and failed')
            login_message = {'message':"your username or password or both wrong."}
            return render(request, 'first_app/login.html' , context=login_message)
    else:
        return render(request, 'first_app/login.html')

@login_required
def special(request):
    return HttpResponse("you are loggged in !!")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('first_app:lvl4index'))

class IndexView(TemplateView):
    template_name = 'first_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "this is from context dictionsry"
        return context