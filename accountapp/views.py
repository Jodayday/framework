# 로그인 확인 데코레이터
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.list import MultipleObjectMixin
# User create file
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import hi
from articleapp.models import Article

# Create your views here.

has_ownership = [login_required, account_ownership_required]


@login_required
def index(request):

    if request.method == "POST":

        temp = request.POST.get('hi_input')
        new_hi = hi()
        new_hi.text = temp
        new_hi.save()
        return redirect(reverse('accountapp:hi'))
    hi_list = hi.objects.all().order_by('-pk')
    return render(request, 'accountapp/hi.html', context={'hi_list': hi_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'
    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(has_ownership, name='get')
@method_decorator(has_ownership, name='post')
class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountUpdateForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, name='get')
@method_decorator(has_ownership, name='post')
class AccountDeleteview(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hi')
    template_name = 'accountapp/delete.html'
