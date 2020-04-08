from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.


def index(response, id):
    ls = TodoList.objects.get(id=id)
    # item = ls.item_set.get(id=1)
    
    # {"save":["save"],"c1":['"clicked"], ...}
    
    if ls in response.user.todolist.all():
        if response.method == 'POST':
            # save and add
            print(response.POST)
            if response.POST.get('save'):
                # loop through all items in todo list and check ids and buttons
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) =="clicked":
                        item.complete = True # update
                    else:
                        item.complete = False
                        
                    item.save()
                        
            elif response.POST.get('newItem'):
                # add
                txt = response.POST.get('new')
                # validate
                if len(txt) > 2:
                    ls.item_set.create(text=txt,complete=False)
                else:
                    print('Invalid Input')
                
        return render(response, "main/list.html", {"ls": ls})
    return render(response, "main/view.html", {})

def v1(response):
    return HttpResponse("<h1>Views 1</h1>")

def home(response):
    return render(response, "main/home.html", {})

def create(response): # res var knows if get or post
    if(response.method == 'POST'):
        # print(response.user)
        # response.user 
        # gives user and can run is auth and get user stuff
        # can be passed in params
        form = CreateNewList(response.POST) 
        # contains all inputs and stored in dict
        # set to what is received
        if form.is_valid():
            n = form.cleaned_data['name'] # access the data and un-encrypt
            t = TodoList(name=n)
            t.save() # creates new todo list
            response.user.todolist.add(t) # map list to user
        
        # redirect to page with data id
        return HttpResponseRedirect("/%i" %t.id)
            
        
    else: # GET
        form = CreateNewList()
    return render(response,"main/create.html",{"form":form})


def view(response):
    return render(response,"main/view.html",{})


