from msilib.schema import ListView
from pyexpat import model
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Post

class PostListView(ListView):
    model= Post

class PostCreateView(CreateView):
    model=Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model=Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(UpdateView):
    model=Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")    

# Create your views here.
