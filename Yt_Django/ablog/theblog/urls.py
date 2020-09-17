from django.urls import path
from . import views
from .views import HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    #path('', views.home ,name='home'),
    path('',HomeView.as_view(),name='home'),
    path('article/(?P<pk>\d+)$', ArticleDetailView.as_view(),name='article-detail'),
    path('add_post/', AddPostView.as_view(),name='add_post'),
    path('article/edit/(?P<pk>\d+)$', UpdatePostView.as_view(),name='update_post'),
    path('article/delete/(?P<pk>\d+)$', DeletePostView.as_view(),name='delete_post'),



]
