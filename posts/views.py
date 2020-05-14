from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import PostItem
from posts.forms import AddPost


def index(request):
    data = PostItem.objects.order_by('date')
    # Matt suggested placing form data in index to display to homepage
    form = AddPost()
    if request.method == "POST":
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    return render(request, 'index.html', {'form': form, 'data': data})


def post_details(request, id):
    html = 'post_details.html'
    post = PostItem.objects.get(id=id)
    return render(request, html, {'post': post})


def like_view(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.results += 1
    post.save()
    return HttpResponseRedirect(reverse('post_details', kwargs={'id': post_id}))


def dislike_view(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.results -= 1
    post.save()
    return HttpResponseRedirect(reverse('post_details', kwargs={'id': post_id}))


def add_post(request):
    form = AddPost()
    if request.method == "POST":
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))
    return render(request, 'index.html', {'form': form})


def boast_view(request):
    data = PostItem.objects.filter(boast_or_roast=True)
    return render(request, 'index.html', {'data': data})


def roast_view(request):
    data = PostItem.objects.filter(boast_or_roast=False)
    return render(request, 'index.html', {'data': data})


def vote_view(request):
    data = PostItem.objects.order_by('-results')
    return render(request, 'index.html', {'data': data})
