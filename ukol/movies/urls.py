from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.MovieList.as_view(), name='list'),
    path('detail/<int:pk>', views.MovieDetail.as_view(), name='detail'),
    path('movie/create/', views.MovieCreate.as_view(), name='movie-create'),
    path('movie/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie-update'),
    path('movie/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie-delete'),
]
