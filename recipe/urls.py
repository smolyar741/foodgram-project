from django.urls import path

from . import views

urlpatterns = [
    #path('add/ingredient', views.ingredients),
    path("", views.index, name="index")
]