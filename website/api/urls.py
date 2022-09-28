from django.urls import path
from . import views
urlpatterns = [
    path('',views.get_routes),
    path('posts/', views.get_posts),
    path('posts/<slug:slug>', views.get_post),
]
