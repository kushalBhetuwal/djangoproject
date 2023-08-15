from django.shortcuts import render, HttpResponse

#create your views here:

def index(request):
    context ={
        'movies': ['titanic', 'topgun', 'casino']
    }
    return render(request, 'movies/index.html' , context)

def about(request):
    context ={
        'movies':['oppenheimer', 'barbie', 'mission impossible']
    }
    return render(request, 'movies/about.html', context)