from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm
from django.template  import context



# Create your views here.

def contact(request):  # 127.0.0.1:8000/
    mydata=Datas.objects.all()
    if(mydata!=""):
        return render(request,"contact.html",{"datas":mydata})
    else:
        return render(request,"contact.html")    
      
    

def addData(request):
    if request.method=="POST":
        fname=request.POST["name"]
        number=request.POST["number"]
        address=request.POST["address"]
        mail=request.POST["mail"]
        
        obj=Datas()
        obj.Name=fname
        obj.Number=number
        obj.Address=address
        obj.Mail=mail
        obj.save()
        mydata=Datas.objects.all()
        return redirect("index")
    return render(request,"contact.html")



def home(request):
     return render(request, 'home.html')

def about(request):
    return HttpResponse("welcome to my about page")
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def aboutpage(request):
    a = loader.get_template('about.html')
    return HttpResponse(a.render())
def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())
def orderpage(request):
    template = loader.get_template('orderpage.html')
    return HttpResponse(template.render())
def logout(request):
    template = loader.get_template('logout.html')
    return HttpResponse(template.render())
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log innow!')    
            return redirect('login')
    else:
            form = UserRegistrationForm()
            context = {'form': form}
            return render(request, 'register.html',context)
