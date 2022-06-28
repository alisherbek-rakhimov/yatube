from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from posts.models import Post


def index(request):
    latest = Post.objects.order_by("-pub_date")[:11]
    return render(request, "index.html", {"posts": latest})
