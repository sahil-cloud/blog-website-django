from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm,LoginUser,AddPost,UpdatePost
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session
from .models import Post
# Create your views here.


def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html',{'posts':posts})


def about(request):
    return render(request, 'blog/about.html')


def dashboard(request):
    if request.user.is_authenticated:
        name = request.session['name']
        posts = Post.objects.filter(author=name)
        return render(request, 'blog/dashboard.html',{'name':name,'posts':posts}) 
    else:
        return HttpResponseRedirect('/login')


def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Congratulations! You have become an author. Now Login to continue..')
                form.save()
                form = SignUpForm()
        else:
            form = SignUpForm()
        return render(request, 'blog/signup.html',{'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def login_user(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = LoginUser(request=request , data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                passd = form.cleaned_data['password']
                user = authenticate(username=uname , password=passd)
                if user is not None:
                    login(request,user)
                    request.session['name'] = uname
                    messages.success(request,'Successfully Logged in')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginUser()
        return render(request, 'blog/login.html', {'form':form})
    else:
        return HttpResponseRedirect('/dashboard/')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def AddPost1(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = AddPost(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                desc = form.cleaned_data['desc']
                author = request.session['name']
                fm = Post(author=author,title=title,desc=desc)
                fm.save()
                msg = 'Post Added Successfully'
                form = AddPost()
        else:
            form = AddPost()
            msg = ''

        return render(request, 'blog/addPost.html',{'form':form,'msg':msg})
    else:
        return HttpResponseRedirect('/login/')


def DelPost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            post = Post.objects.get(pk=id)
            post.delete()
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')


def UpdatePost1(request,id):
    if request.user.is_authenticated:
        if request.method == "POST":
            ins = Post.objects.get(pk=id)
            # print(ins)
            form = UpdatePost(request.POST,instance=ins)
            # form = UpdatePost(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Post Updated Successfully')
                return HttpResponseRedirect('/dashboard/')
        else:
            ins = Post.objects.get(pk=id)
            # print(ins.author)
            form = UpdatePost(instance=ins)

        return render(request, 'blog/editPost.html', {'form': form})
    else:
        return HttpResponseRedirect('/login/')
