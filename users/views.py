from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import PersonForm,UserForm
from .models import Person
# from django.views.generic import CreateView
from .models import Person
# Create your views here.

# class PersonCreateView(CreateView):
#     model = Person
#     fields = ('name', 'email', 'job_title', 'bio')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = PersonForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            username = user_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        user_form = UserForm(data=request.POST)
        profile_form = PersonForm(data=request.POST)

    context ={
        'user_form':user_form,
        'profile_form':profile_form
    }

    return render(request,'users/register.html',context)

def person_detail_view(request):
    obj = Person.objects.get(id=1)
    context = {
        'FirstName': obj.first_name,
        'email':obj.email,
        'LastName':obj.last_name
    }
    return render(request,'users/detail.html',context)

