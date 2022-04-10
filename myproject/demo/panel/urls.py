from django.urls import path
from panel import views

app_name = "panel"

urlpatterns = [
    path('', views.home, name = "home"),
    path('list/', views.list, name = "list"),
    path('edit/<int:pk>/', views.edit, name = "edit"),
    path('delete/<int:pk>/', views.delete, name = "delete")
]
