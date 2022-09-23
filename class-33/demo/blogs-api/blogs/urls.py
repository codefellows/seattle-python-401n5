from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('/<int:pk>', BlogDetail.as_view(), name='blog_detail')
]
