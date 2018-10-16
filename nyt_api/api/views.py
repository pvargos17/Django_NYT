from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/profile')

    if request.method == 'POST':
        if 'signupform' in request.POST:
                signupform = UserCreationForm(data=request.POST)
                signinform = AuthenticationForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    return redirect('/')
        else:
            signupform = UserCreationForm()
            signinform = AuthenticationForm(data=request.POST)

            if signinform.is_valid():
                login(request, signinform.get_user())
                return redirect('/')


    signupform = UserCreationForm()
    signinform = AuthenticationForm()

    return render(request, 'frontpage.html', {'signupform': signupform,
                                              'signinform': signinform})


def signout(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request, 'profile.html')
