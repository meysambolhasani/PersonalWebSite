from django.urls import path
from . import views

urlpatterns = [
    path('',views.last_posts,name='last-posts'),
    path('all-posts/', views.all_posts, name='all-post'),
    path('single-post/<slug:slug>', views.single_post, name='single-post'),
    path('create-post', views.create_post, name='create-post'),
    path('update-post/<slug:slug>', views.update_post, name='update-post'),
    path('delete-post/<slug:slug>', views.delete_post, name='delete-post'),

]
