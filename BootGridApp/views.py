from django.shortcuts import render

# Create your views here.
# only necessary to render the pages since the only real user interface is the buttons with don't really have input
def index(request):
    return render(request,'BootGridApp/index.html')

def pageTwo(request):
    return render(request,'BootGridApp/page2.html')

def pageThree(request):
    return render(request,'BootGridApp/page3.html')