from django.shortcuts import redirect, render
from django.urls import reverse

from accountapp.models import hi

# Create your views here.

def index(request):
    hi_list=hi.objects.all().order_by('-pk')
    if request.method == "POST":

        temp = request.POST.get('hi_input')
        new_hi = hi()
        new_hi.text = temp
        new_hi.save()



        return redirect(reverse('accountapp:hi'))




    return render(request, 'accountapp/hi.html',context={'hi_list':hi_list})