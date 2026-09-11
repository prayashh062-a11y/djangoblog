from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html', {'title': 'Djangoblog Homepage'})

def about(request):
    return render(request, 'blog/about.html', {'content': 'Djangoblog team'})
def about(request):
    return render(request, 'blog/contact.html', {'abc': 'Djangoblog contact team'}) 