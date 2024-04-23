from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


# Create your views here.
def index(xx):
    users = User.objects.all()
    context = {"usuarios": users}
    return render(xx, 'index.html', context)

def user_create_view(request):
    if request.method == "GET":
        contexto = {"Form": UserCreateForm()}
        return render(request, "create_user_form.html", contexto)
    elif request.method == "POST":
        form = UserCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            group_user = form.cleaned_data['group_user']
            usuarios = User.objects.all()
            invalid_usernames = []
            for usuario in usuarios:
                invalid_usernames.append(usuario.name)
            if name in invalid_usernames:
                return HttpResponse(f"<h3>ese nombre ya esta tomado</h3>")
            else:
                nuevo_user = User(name=name, password=password, group_user=group_user)
                nuevo_user.save()
                return redirect(index)

def group_create_view(request):
    if request.method == "GET":
        contexto = {"Form": GroupCreateForm()}
        return render(request, "create_group_form.html", contexto)
    elif request.method == "POST":
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            alias = form.cleaned_data['alias']
            description = form.cleaned_data['description']
            creator = form.cleaned_data['creator']

            nuevo_group = Group(alias=alias, description=description, creator=creator)
            nuevo_group.save()
            return redirect(index)


def group_view(request, userid):
    user = User.objects.filter(id=userid)[0]
    group = user.group_user
    messages = Message.objects.filter(group=group).all()
    context = {'user':user,"userid":userid, "group":group, "messages":messages, "Form":SendMessageForm()}
    if request.method == "GET":
        return render(request, "group.html", context)
    elif request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            message = Message(content=content, group=group, author=user)
            message.save()
        return render(request, "group.html", context)

def login_view(request):
    if request.method == "GET":
        form = AuthenticationForm()
    elif request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.user_cache
            if user is not None:
                login(request, user)
                return redirect('home')
    return render(request, 'login.html', {"form":form})
