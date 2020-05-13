from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('like/<int:post_id>/', views.like_view),
    path('post_details/<int:id>', views.post_details, name='post_details')
]
