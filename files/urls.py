from django.urls import path
from files import views

urlpatterns = [path("values/", views.FileView.as_view())]