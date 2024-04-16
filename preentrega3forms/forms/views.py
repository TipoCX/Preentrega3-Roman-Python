from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *

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
            nuevo_user = User(name=name, password=password)
            nuevo_user.save()
            return HttpResponse(f"<h3>{nuevo_user.id}</h3>")
