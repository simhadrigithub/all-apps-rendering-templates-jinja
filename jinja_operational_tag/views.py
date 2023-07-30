from django.shortcuts import render

# Create your views here.
d={'a':20,'b':30,'c':40}
def jinja_operational(request):
    return render(request,'jinja_operational.html',context=d)
