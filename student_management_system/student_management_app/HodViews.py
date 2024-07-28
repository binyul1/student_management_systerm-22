from django.shortcuts import render


def admin_home(request):
    return render(request,'hod_template/home_content.html')

def add_staff(request):
    return render(request,'hod_template/add_staff_template.html')

def add_staff_save(request):
    if request.method!="POST":
        return HttpResponse("Method Not Allowed")
    else:
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        first_name=request.POST.get('first_name')
        first_name=request.POST.get('first_name')
        username=request.POST.get('username')
        address=request.POST.get('address')
