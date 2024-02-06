from django.shortcuts import render


# Create your views here.
def home(request):

    return render(request, 'blog/index.html')


def blogs(request):

    return render(request, 'blog/blogs.html')


def blog_single(request):

    return render(request, 'blog/blog-single.html')