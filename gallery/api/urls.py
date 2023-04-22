from django.urls import path

from api.views import add, remove

urlpatterns = [
    path('add/', add, name='add'),
    path('remove/', remove, name='remove'),
]