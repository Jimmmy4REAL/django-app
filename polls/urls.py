from django.urls import path
from . import views

# to inlclude the func declare in views
urlpatterns = [
    path("", views.index, name="index"),
]