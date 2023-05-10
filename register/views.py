from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import HttpResponseRedirect, redirect, render

from .forms import EditUserProfileForm


def homepage(request):
    if not request.user.is_authenticated:

        if request.method == 'POST':
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')
            email = request.POST.get('email')

            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                print("Emmail already exists")
                return redirect('/')
            if password != password2:
                messages.info(request, "Passwords do not match")
                return redirect('/')

            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=fname, last_name=lname)
                user.save()
                messages.success(request, "User Created")
                print('User created')
                return redirect('login')

        return render(request, 'homepage.html')
    else:
        return HttpResponseRedirect(redirect_to='userprofile')
        # return HttpResponseRedirect(redirect_to='login')


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                # return redirect('/userprofile/')
                # return redirect('/')
                return HttpResponseRedirect(redirect_to='/')
            else:
                messages.info(request, "Invalid username or password")
                return redirect('login')
            
        return render(request,'login2.html') # ===========================================
    else:
        # return HttpResponseRedirect(redirect_to='userprofile')
        return HttpResponseRedirect(redirect_to='/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_form = EditUserProfileForm(data = request.POST, instance=request.user)

            if user_form.is_valid():
                messages.success(request=request, message="Profile Updated Successfully!!")
                user_form.save()
        else:
            user_form = EditUserProfileForm(instance=request.user)

        context = {
            'user_form' : user_form
        }

        return render(request=request, template_name="user_profile.html", context=context)
    
    else:
        return HttpResponseRedirect(redirect_to='/login/')


def logout(request):
    auth.logout(request)
    return redirect('/')