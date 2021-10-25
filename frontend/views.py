import os

from django.views import generic
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')

        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request,'logout.html')


def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'admin_page.html')

def donate_page(request):
    return render(request, 'donate.html')

def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
    else:
        f = UserCreationForm()
    return render(request, 'register.html', {'form': f})

def gallery(request):
    path="/home/habitual/alumni_site/frontend/static/img"  # insert the path to your directory
    img_list = os.listdir(path)
    context = {'images': img_list}
    return render(request, 'gallery.html', context)