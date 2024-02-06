from django.urls import path
from .views import home, blogs, blog_single

urlpatterns = [
    path('home', home, name='home'),
    path('blogs', blogs, name='blogs'),
    path('blog-single', blog_single, name='blog-single'),
]
