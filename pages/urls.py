from django.urls import path
from .views import BlogDetailView, HomePageView, BlogListView

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home'),
    path('blog/', BlogListView.as_view(), name = 'blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail')
]
