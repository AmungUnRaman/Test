
from .models import Post, Comment, Category, PostCategory
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

from datetime import datetime
from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator

class Posts(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 1
    form_class = PostForm

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['filter'] = PostFilter(self.request.GET,
                                          queryset=self.get_queryset())
        context['postCategories'] = Category.objects.all()
        context['form'] = PostForm()
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()
        context['comment_list'] = Comment.objects.filter(commentPost=self.kwargs['pk'])

        return context

class PostSearch(ListView):
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    queryset = Post.objects.all()  # Н

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            'time_now'] = datetime.now()
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())
        return context

class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'