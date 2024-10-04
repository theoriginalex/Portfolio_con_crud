from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
# Create your views here.


def post_normal(request):
    post = Post.objects.all()
    return render(request, 'blog/blog.html', {'post': post})


def detalle_post(request, post_id):
    posts = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'posts': posts})


# Vista para el formulario de Post
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog:posts')  # Cambia 'post_list' al nombre de la vista donde quieres redirigir después de guardar
    else:
        form = PostForm()
    return render(request, 'formularios/form_post.html', {'form': form})



