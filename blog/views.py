from django.views.generic import DetailView, ListView

from .models import Post

class PostListView(ListView):
    model = Post

class PostDetailVire(DetailView):
    model = Post