from os import path
from . import views

app_name = 'events'

urlpatterns = [
    path('show_post/', views.show_post, name='show_post'),
]
