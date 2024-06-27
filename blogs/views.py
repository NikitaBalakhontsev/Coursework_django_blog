from .models import Blog
import random
from django.shortcuts import render
from django.views.generic import DetailView


from django.http import JsonResponse
from django.template.loader import render_to_string

def resources(request):
    blogs = Blog.objects.all()
    return render(request, 'blogs/resources.html', {'blogs':blogs})


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blogs/blog-detail.html"
    context_object_name = 'blog'
