from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import authenticate

#from student_management_app.EmailBackEnd import EmailBackend

# Create your views here.
def showDemoPage(request):
    return render(request,'demo.html')
def showLoginPage(request):
    return render(request,'login_page.html')
def doLogin(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else: 
        user=authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
        if user!=None:
            login(request,user)
            return HttpResponse("Email:"+request.POST.get("email")+" Password: "+request.POST.get("password"))
        else:

            return HttpResponse("Invalid Login")

def GetUserDetails(request):
    if request.user!=None:
        return HttpResponse("User: "+request.user.email+" usertype: "+request.user.usertype)
    else:
        return HttpResponse("Please Login First")
    
def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")