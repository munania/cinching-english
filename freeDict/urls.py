from django.urls import path
from . import views

urlpatterns = [
    path('', views.freeDict, name='freedict'),
]