from django.urls import path
from . import views

app_name = "sheeeesh"
urlpatterns = [
    path('', views.index, name='index'),
]