from django.urls import path 
from .views import PostL

urlpatterns=[
    path("",PostL.as_view(),name="post_l"),
]