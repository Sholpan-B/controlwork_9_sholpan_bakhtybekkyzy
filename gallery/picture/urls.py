from django.urls import path

from picture.views import PhotoListView, PhotoCreateView, PhotoDetailView, PhotoDeleteView, PhotoUpdateView

urlpatterns = [
    path("", PhotoListView.as_view(), name='index'),
    path('photo/add/', PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>', PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo_delete'),
]
