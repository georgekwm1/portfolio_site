from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('view/<int:pk>/',views.view, name='view'),
]