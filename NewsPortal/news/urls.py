from django.urls import path
from . views import Posts, PostDetail, PostCreateView, PostSearch, PostUpdateView, PostDeleteView


urlpatterns = [
    path('', Posts.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='post'),
    path('search/', PostSearch.as_view(), name = 'search' ),
    path('add/', PostCreateView.as_view(), name='post_create'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    ]