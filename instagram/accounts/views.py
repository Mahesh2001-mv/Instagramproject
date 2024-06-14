from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from . models import UserDetails, follower, following
from django.contrib import messages



def registerUser(request):
    if request.method == 'POST':
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        dateOfBirth = request.POST.get('dateOfBirth')
        mobile = request.POST.get('mobile')
        confirmPassword = request.POST.get('confirmPassword')
        profilepic=request.FILES.get('profilepic')

        if password == confirmPassword:
            newuser = User.objects.create_user(
            first_name=firstName,
            last_name=lastName,
            username=username,
            password=password,
            email=email
            )

            UserDetails.objects.create(
            dateOfBirth=dateOfBirth,
            mobile=mobile,
            profilepic=profilepic,
            user_id=newuser.id
            )
        else:
            messages.add_message(request,messages.ERROR,"Password mismatch")
            return redirect('register')

    return render(request, 'accounts/register.html')

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('upload')

    return render(request, 'accounts/login.html')

def profile(request, username):
    try:
        user = User.objects.get(username=username)

        followers = len(follower.objects.filter(u_id = user))
        followings = len(following.objects.filter(u_id = user))
    except User.DoesNotExist:
        return redirect('notfound')
    return render(request, 'accounts/profile.html', {'user': user, 'followers':followers, 'following':followings})

def follow(request,id):
    following.objects.create(
        u_id=request.user,
        f_id=id
    )
    follower.objects.create(
        u_id=User.objects.get(id=id),
        f_id=request.user.id
    ) 
    return render(request,'accounts/profile.html')


