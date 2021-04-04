from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# import requests
# import json

# api_key = 'BQwlCAeXaR55mC-EAmnEHBt6r7VD32-Bev9pPHvDN7tHLykQXG0I6RMPIBx4ShNBb7G0eILSzqlWa2iHhw2KVEzCqvyhxgdv3agR_5haNWyftS_j85dzsmCfnGFpYHYx'
# headers = {
#     'Authorization': 'Bearer %s' % api_key
# }



def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create your views here.
