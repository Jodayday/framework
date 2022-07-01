from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUpdateForm


from accountapp.models import hi

# Create your views here.


def index(request):
    hi_list = hi.objects.all().order_by('-pk')
    if request.method == "POST":

        temp = request.POST.get('hi_input')
        new_hi = hi()
        new_hi.text = temp
        new_hi.save()
        return redirect(reverse('accountapp:hi'))
    return render(request, 'accountapp/hi.html', context={'hi_list': hi_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'accountapp/update.html'
