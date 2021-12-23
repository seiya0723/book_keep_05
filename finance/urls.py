from django.urls import path
from . import views

app_name    = "finance"
urlpatterns = [
    path('', views.index, name="index"),
    path('category/',views.category,name="category"),
    path('edit/<int:pk>', views.edit, name="edit"),
]