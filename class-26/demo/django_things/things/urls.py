from django.urls import path
from .views import HomePageView, AboutView, OrderView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('order', OrderView.as_view(), name='order'),
]
