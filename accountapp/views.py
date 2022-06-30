from django.shortcuts import render

from accountapp.models import hi

# Create your views here.

def index(request):
    
    if request.method == "POST":

        temp = request.POST.get('hi_input')
        new_hi = hi()
        new_hi.text = temp
        new_hi.save()



        return render(request, 'accountapp/hi.html',context={'new_hi':new_hi})




    return render(request, 'accountapp/hi.html',context={'text':'GET요청완료'})