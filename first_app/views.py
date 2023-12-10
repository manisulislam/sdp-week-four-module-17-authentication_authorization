from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
# Create your views here.
def signUp(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                messages.success(request, f"Your account has been created! You are now able to log in")
                form.save()
                
        else:
            form = RegisterForm()
        return render(request,'signup.html', {"form": form})
    else:
        return redirect("profile")


def signIn(request):
    if request.user.is_authenticated:
        return redirect("profile")
    else:
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    return redirect("profile")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                form = AuthenticationForm()
            return render(request, "signIn.html", {"form": form})
    


def profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html',{'user':request.user})
    else:
        return redirect("signIn")

def sign_out(request):
    logout(request)
    return redirect("signIn")


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'pass_change.html', {
        'form': form
    })

def without_old_pass_change(request):
    if request.method == 'POST':
        form = SetPasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(request.user)
    return render(request, 'pass_change.html', {
        'form': form
    })