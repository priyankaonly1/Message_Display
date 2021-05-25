from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages 

# Create your views here.


def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            # longcut method
            messages.add_message(request, messages.SUCCESS, 'Your account has been created')
            # shortcut method
            messages.info(request, 'Now you can login')   

            messages.error(request, 'This is error') 

            # setting for debug message
            messages.set_level(request, messages.DEBUG)
            messages.debug(request,'This is debug')

            fm = StudentRegistration()   
    else:
        fm = StudentRegistration()

    return render(request, 'enroll/userregistration.html', {'form':fm})