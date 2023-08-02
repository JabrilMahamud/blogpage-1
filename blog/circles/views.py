from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, RegistrationForm, PostForm

from .models import Post

def home(request):
    return render(request, 'home.html')
from django.contrib import messages  # Import messages

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('timeline')
            else:
                messages.error(request, 'Invalid username or password')  # Add this line
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('timeline')  # Redirect to the timeline page
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


@login_required
def timeline(request, id=None):
    if id:
        post = get_object_or_404(Post, id=id)
        return render(request, 'timeline.html', {'post': post})
    else:
        posts = Post.objects.all()
        return render(request, 'timeline.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            content = form.cleaned_data['content']
            file = form.cleaned_data['file']

            if not content and not file:
                messages.error(request, "Either content or a file is required.")
                return render(request, 'create_post.html')

            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('timeline')

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})