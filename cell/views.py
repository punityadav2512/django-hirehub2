# from turtle import title
from datetime import datetime
from email.mime import image
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib import messages
from company.models import Post
from cell.models import Posts, Profile
User = get_user_model()
# Create your views here.


def index(request):
    return render(request, 'cell/index.html')


def home(request):
    cell_posts = Posts.objects.all()
    profile = Profile.objects.filter(user=request.user)
    # company_posts=Post.objects.all()
    # allposts=cell_posts | company_posts
    return render(request, 'cell/home.html', {'allposts': cell_posts, 'profile': profile})


def register(request):
    if request.method == 'POST':
        # username=request.POST['email']
        first_name = request.POST['college_name']
        # last_name=request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Alredy Used')
                return redirect('register_cell')
            else:
                user = User.objects.create_user(
                    username=email, first_name=first_name, email=email, password=password, is_cell=True)
                user.save()
                return redirect('login_cell')

        else:
            messages.info(request, 'Password does not match , Try again')
            return redirect('register_cell')
    else:
        return render(request, 'cell/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_cell == True:
                auth.login(request, user)
                return redirect('home_cell')
            else:
                messages.info(request, 'Credentials Invalid')
                return redirect('login_cell')

        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login_cell')
    else:
        return render(request, 'cell/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES['uploadfromPC']
        user = request.user

        new_post = Posts(title=title, content=content, dated=datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'), author=user, image=image)
        new_post.save()
        return redirect('home_cell')
    return render(request, 'cell/addpost.html')


def profile(request):
    if request.method == 'POST':
        bio = request.POST['bio']
        location = request.POST['location']
        url = request.POST['url']
        image = request.FILES['uploadfromPC']
        user = request.user

        if Profile.objects.filter(user=user).exists():
            Profile.objects.filter(user=user).delete()
            new_profile = Profile(bio=bio, location=location, url=url, user=user, dated=datetime.now(
            ).strftime('%Y-%m-%d %H:%M:%S'), image=image)
            new_profile.save()
        else:
            new_profile = Profile(bio=bio, location=location, url=url, user=user, dated=datetime.now(
            ).strftime('%Y-%m-%d %H:%M:%S'), image=image)
            new_profile.save()
    cellposts = Profile.objects.filter(user=request.user)
    # my_profile=Profile.objects.filter(user=request.user)
    return render(request, 'cell/profile.html', {'cellposts': cellposts})
