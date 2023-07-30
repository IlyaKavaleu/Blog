from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('show_post/', views.show_post, name='show_post'),
    path('posts/<int:post_id>', views.one_post, name='one_post'),
]
