from django.urls import path
from .views import MovieListView, MovieDetailView, MovieCreateView, MovieDeleteView, MovieUpdateView

urlpatterns = [
    path('', MovieListView.as_view(), name='list_movie'),
    path('<int:pk>/', MovieDetailView.as_view(), name='detail_movie'),
    path('create/', MovieCreateView.as_view(), name='create_movie'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='update_movie'),
    path('delete/<int:pk>/', MovieDeleteView.as_view(), name='delete_movie'),
]
