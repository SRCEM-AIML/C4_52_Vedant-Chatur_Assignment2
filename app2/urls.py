from django.urls import path
from .views import sample2

urlpatterns = [
    path('sample2/', sample2, name='sample2'),
]