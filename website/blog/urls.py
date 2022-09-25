from django.urls import path
from . import views

urlpatterns = [
    path('',views.last_posts,name='last-posts'),
    path('all-posts/', views.all_posts, name='all-post'),
    path('single-post/<slug:slug>', views.single_post, name='single-post'),

]
