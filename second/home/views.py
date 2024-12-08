from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request) :

    context = {

        "variable1":"Abhi You Are Doing Well Buddy",
        "variable2":"Carry On Buddy"
    }

    return render(request, 'index.html', context)
    
    # return HttpResponse("This is home page")

def about(request) :
    
    return render(request, 'about.html')

def contact(request) :

   return render(request, 'contact.html')

def services(request) :

    return render(request, 'services.html')

