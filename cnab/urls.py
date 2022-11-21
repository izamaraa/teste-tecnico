from django.urls import path
from cnab import views

urlpatterns = [path("files/", views.CnabView.as_view())]