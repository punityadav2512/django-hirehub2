from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib import messages
from datetime import datetime
from company.models import Post,Profile
from cell.models import Posts
User=get_user_model()
# Create your views here.
def index_landing(request):
    return render(request,'index.html')

def home(request):
    # cell_posts=Posts.objects.all()
    company_posts=Post.objects.all()
    profile=Profile.objects.filter(user=request.user)
    # allposts=cell_posts.union(company_posts)
    return render(request,'company/home.html',{'allposts':company_posts,'profile':profile})

def index(request):
    return render(request,'company/index.html')


def register(request):
    if request.method =='POST':
        # username=request.POST['email']
        first_name=request.POST['company_name']
        # last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']

        if password == password2 :
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Alredy Used')
                return redirect('register_company')
            else:
                user=User.objects.create_user(username=email,first_name=first_name,email=email,password=password,is_company=True)
                user.save();
                return redirect('login_company')

        else:
            messages.info(request,'Password does not match , Try again')
            return redirect('register_company')
    else:
        return render(request,'company/register.html')
        

    

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_company==True:
                auth.login(request,user)
                return redirect('home_company')
            else:
                messages.info(request,'Credentials Invalid')
                return redirect('login_company')

        else:
            messages.info(request,'Credentials Invalid')
            return redirect('login_company')
    else:
        return render(request,'company/login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def post(request):
    if request.method == 'POST':
        title=request.POST['title']
        content=request.POST['content']
        image=request.FILES['uploadfromPC']
        user=request.user

        new_post=Post(title=title,content=content,dated=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),author=user,image=image)
        new_post.save()
        return redirect('home_company')
    return render(request,'company/addpost.html')


# def profile(request):
#     user=request.user
#     companyposts=Post.objects.filter(author=user)

#     return render(request,'company/profile.html',{'companyposts':companyposts})

def profile(request):
    if request.method == 'POST':
        bio=request.POST['bio']
        location=request.POST['location']
        url=request.POST['url']
        image=request.FILES['uploadfromPC']
        user=request.user

        if Profile.objects.filter(user=user).exists():
            Profile.objects.filter(user=user).delete()
            new_profile=Profile(bio=bio,location=location,url=url,user=user,dated=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),image=image)
            new_profile.save()
        else:
            new_profile=Profile(bio=bio,location=location,url=url,user=user,dated=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),image=image)
            new_profile.save()
    companyposts=Profile.objects.filter(user=request.user)
    # my_profile=Profile.objects.filter(user=request.user)
    return render(request,'company/profile.html',{'companyposts':companyposts})


def search(request):
    query=request.GET['query']
    if len(query)>50:
        allposts=[]
    else:
        allposts=User.objects.filter(first_name__icontains=query)
    context={'allposts': allposts,'query':query}
    return render(request,'company/search.html',context)