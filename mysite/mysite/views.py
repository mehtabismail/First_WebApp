from django.shortcuts import render, HttpResponse

#def Home(request):
#    return HttpResponse('<h1>My First Website</h1>')

def Home(request):
    return render(request, 'home.html')

def result(request):
    name = request.GET['user_name']
    age = request.GET['user_age']
    message = f'hi,{name}, you are {age}, yours old'
    return render(request, 'result.html',{'age':message})
