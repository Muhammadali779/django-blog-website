from django.urls import path

from .views import (
    BlogCreateView,
    BlogDeleteView,
    BlogDetailView,
    BlogsView,
    BlogUpdateView,
    HomeView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("blogs/", BlogsView.as_view(), name="blogs"),
    path("blogs/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blogs/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("delete/", BlogDeleteView.as_view(), name="blog_delete_list"),
    path("delete/<int:id>/", BlogDeleteView.as_view(), name="blog_delete"),
    path("blogs/update/<int:id>/", BlogUpdateView.as_view(), name="blog_update"),
]
