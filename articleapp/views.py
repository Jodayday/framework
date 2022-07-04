
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.views.generic.edit import FormMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from articleapp.decorators import article_ownership_required
from articleapp.models import Article
from articleapp.forms import ArticleCreateForm
from commentapp.forms import CommentCreateForm
# Create your views here.


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreateForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp = form.save(commit=False)
        temp.writer = self.request.user
        temp.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


class ArticleDetailView(DetailView, FormMixin):
    model = Article
    form_class = CommentCreateForm
    template_name = 'articleapp/detail.html'
    context_object_name = 'target_article'


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'target_article'
    form_class = ArticleCreateForm
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse_lazy('articleapp:detail', kwargs={'pk': self.object.pk})


@method_decorator(article_ownership_required, 'get')
@method_decorator(article_ownership_required, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'target_article'
    success_url = reverse_lazy('articleapp:list')
    template_name = 'articleapp/delete.html'


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'articleapp/list.html'
    paginate_by = 5
