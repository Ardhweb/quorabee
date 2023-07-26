from django.shortcuts import render, HttpResponse,redirect

# Create your views here.
from .forms import LoginForm, UserRegistrationForm,  \
                    UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout 



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid ():
 # Create a new user object but avoid saving it yet
            rookie = form.save(commit=False)
 # Set the chosen password
            rookie.set_password(form.cleaned_data['password'])
 # Save the User object
            rookie.save()
            #Profile
           
            # Create the user profile
            profile_created = Profile.objects.create(user=rookie,email=rookie.email) # email is fields name object in profile and rookie.email is value from user model email.
            print(profile_created, 'New User Email Id from User Model form:',rookie.email)
            #return render(request,'account/register_done.html',{'rookie':rookie})
            return redirect("account:login")
    else:
        form = UserRegistrationForm()
    return render(request,'account/register.html',{'form': form})






def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                        username=cd['username'],
                                        password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated successfully')
                    return redirect("home")
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
                                    'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                'account/edit.html',
                {'user_form': user_form,
                'profile_form': profile_form})


def logout_view(request):
  logout(request)
  return redirect('home')