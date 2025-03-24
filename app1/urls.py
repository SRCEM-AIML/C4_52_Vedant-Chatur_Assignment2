from django.urls import path
from .views import home, sample1

urlpatterns = [
    path('', home, name='home'),
    path('sample1/', sample1, name='sample1'),
]