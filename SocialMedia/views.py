from email import message
from django.shortcuts import get_object_or_404, render, redirect
from pkg_resources import to_filename
from requests import post
from SocialMedia.models import *
from SocialMedia.forms import *
from django.contrib import messages

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
# Create your views here.


def index(request):
    return render(request, 'index.html')

@login_required
def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'posts':posts})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        #form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            messages.success(request, f'Usuario {username} creado exitosasmente!')
            return redirect('feed')
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()

    return render(request, 'register.html', {'form':form})


@login_required
def profile(request, username=None):
    current_user = request.user
    if username and username != current_user.username: #preguntamos si existe un usuario y si el usuario es distinto al que esta logeado
        user = User.objects.get(username=username)
        posts = user.posts.all()#traemos todos los post del usuario que no es el que esta logeado
    else:
        posts = current_user.posts.all() #obtenemos los pos hechos por el ususario loggeado
        user = current_user

    return render(request, 'profile.html', {'user':user, 'posts':posts})

@login_required
def post(request):
    current_user = get_object_or_404(User, pk=request.user.pk) #obtenemos el usuario loggeado de la app
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user #asignamos el post al usuario loggeado
            post.save()
            messages.success(request, 'Post created correctly')
            return redirect('feed')
    else:
        form = PostForm()

    return render(request, 'post.html', {'form':form})


@login_required
def follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user
    rel = Relationship(from_user=current_user, to_user=to_user_id)
    rel.save()
    messages.success(request, f"You follow {username}!")

    return redirect(f'/profile/{username}')

@login_required
def un_follow(request, username):
    current_user = request.user
    to_user = User.objects.get(username=username)
    to_user_id = to_user.id
    rel = Relationship.objects.filter(from_user=current_user.id, to_user=to_user_id).get()
    rel.delete()
    messages.info(request, f"You don't follow {username}")

    return redirect(f'/profile/{username}')


@login_required
def edit_profile(request):
    user = request.user
    user_data = User.objects.get(id = user.id)
    user_country = Country.objects.get(user__id = user.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance = user)
        form2 = UserEditCountry(request.POST, instance=user)
        if form.is_valid():
            #Datos que se van a actualizar
            user_data.username = form.cleaned_data.get('username')
            user_data.first_name = form.cleaned_data.get('first_name')
            user_data.last_name = form.cleaned_data.get('last_name')
            user_data.email = form.cleaned_data.get('email')
            user_country.country = form.cleaned_data.get('country')
            user_data.save()
            user_country.save()
            return render(request, 'profile.html')

    else:
        form = UserEditForm(initial={'email': user.email, 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name})
        form2 = UserEditCountry(initial={'country':user.country})
    return render(request, 'edit_profile.html', {'form': form, 'user': user, 'form2':form2})

@login_required
def my_data(request):
    return render(request, 'my_data.html')


@login_required
def edit_avatar(request):
    user = request.user.id
    profile_data = Profile.objects.get(user__id=user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            profile_data.image = form.cleaned_data.get('avatar')
            profile_data.save()
            return render(request, 'profile.html')

    else:
        form = AvatarForm()

    return render(request, 'edit_avatar.html', {'form': form})


@login_required
def edit_pass(request):
    user = request.user
    if request.method == 'POST':
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return render(request, 'profile.html')

    else:
        form = ChangePasswordForm(user = request.user)
    return render(request, 'edit_pass.html', {'form': form, 'usuario': user})