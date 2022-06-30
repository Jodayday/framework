from django.shortcuts import render

# Create your views here.

def index(request):
    
    if request.method == "POST":
        return render(request, 'accountapp/hi.html',context={'text':'POST요청완료'})




    return render(request, 'accountapp/hi.html',context={'text':'GET요청완료'})