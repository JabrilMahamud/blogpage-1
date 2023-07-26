from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, RegistrationForm, PostForm
from .models import Post

def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('timeline')  # Redirect to the template page
            else:
                form.add_error(None, 'Invalid username or password')
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
        # An id is provided, display the specified post
        post = get_object_or_404(Post, id=id)
        return render(request, 'timeline.html', {'post': post})
    else:
        # No id provided, display all posts
        posts = Post.objects.all()
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.save()
                return redirect('timeline')
        else:
            form = PostForm()
        return render(request, 'timeline.html', {'posts': posts, 'form': form})
    
@login_required
def template_page(request):
    # Replace the following line with the actual implementation of your template page
    return render(request, 'timeline.html')
