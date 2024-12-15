from django.urls import path, include
from . import views

urlpatterns = [
    path("atributes/", views.AttributeCreate.as_view(), name="atribute-create"),
]
