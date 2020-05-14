from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('like/<int:post_id>/', views.like_view),
    path('post_details/<int:id>', views.post_details, name='post_details'),
    path('form/', views.add_post, name='form'),
    path('dislike/<int:post_id>/', views.dislike_view),
    path('boast/', views.boast_view, name='boast'),
    path('roast/', views.roast_view, name='roast'),
    path('vote/', views.vote_view, name='votes'),
]
