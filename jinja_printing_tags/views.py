from django.shortcuts import render

# Create your views here.

d={'name':'simhadri','age':21,'degree':'bsc(mpcs)','framework':'django'}
def jinja_printing(request):
    return render(request,'jinja_printing.html',context=d)
