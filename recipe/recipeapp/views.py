# recipes/views.py

from django.shortcuts import render
from .models import UsersTable


def login(request):
    obj = UsersTable()
    users = UsersTable.objects.all()
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        userdata = [i for i in users if username == i.username]
        if len(userdata)==0:
            print("login",username, password)
            obj = UsersTable()
            obj.username = username
            obj.password = password
            obj.save()
            users = UsersTable.objects.all()
            return render(request,'home.html',{"all":users})
    if request.method=='GET':
        if "id" in request.GET:
            id = request.GET["id"]
            user_data = UsersTable.objects.get(id=id)
            user_data.delete()
            users = UsersTable.objects.all()
            return render(request,'home.html',{"all":users})
    return render(request,'home.html',{"all":users})

def home(request):
    obj = UsersTable()
    users = UsersTable.objects.all()
    if request.method == 'POST':
        print("inn22")
        username = request.POST["username"]
        password = request.POST["password"]
        print(username, password)
        all_users = UsersTable.objects.all()
        userdata = [i for i in all_users if username == i.username and password==i.password ]
        if userdata:
            return render (request,'result.html',{"username":userdata[0].username,"password":userdata[0].password,"id":userdata[0].id})
        else:
            users = UsersTable.objects.all()
            return render (request,'home.html',{"all":users,"msg":"Incorrect Credential! Try Again"})
        
    if request.method == 'GET':
        username = request.GET["username"]
        password = request.GET["password"]
        id = request.GET["id"]
        user_data = UsersTable.objects.get(id=id)
        user_data.id = id
        user_data.username = username
        user_data.password = password
        user_data.save()
        return render(request,'home.html',{"all":users})

def profile_edit(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    id = request.GET.get('id')
    return render(request,'profile_edit.html',{"username":username,"password":password,"id":id})
    

def register(request):
    return render (request,'register.html')

def details(request):
    id = request.GET["id"]
    return render(request,'details.html')


