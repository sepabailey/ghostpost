from django.shortcuts import render, reverse, HttpResponseRedirect
from posts.models import PostItem
from posts.forms import AddPost


def index(request):
    data = PostItem.objects.all()
    return render(request, 'index.html', {'data': data})


def post_item(request):
    return render(request, 'index.html')


def post_details(request, id):
    html = 'post_details.html'
    post = PostItem.objects.get(id=id)
    return render(request, html, {'post': post})


def like_view(request, post_id):
    post = PostItem.objects.get(id=post_id)
    post.likes += 1
    post.save()
    return HttpResponseRedirect(reverse('post_details', kwargs={'id': post_id}))


def add_post(request):
    html = "genericform.html"
    form = AddPost()
    if request.method == "POST":
        form = AddPost(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))
    return render(request, html, {"form": form})
