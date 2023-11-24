from django.shortcuts import render

# Create your views here.
def kalyan(request):
    return render(request,'kalyan.html')


def job(request):
    return render(request,'job.html')