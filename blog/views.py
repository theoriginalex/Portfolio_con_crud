from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def post_normal(request):
    post = Post.objects.all()
    return render(request, 'blog/blog.html', {'post': post})



def detalle_post(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'posts': posts})




