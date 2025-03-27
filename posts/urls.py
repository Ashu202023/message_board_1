from django.urls import path 
from .views import PostL
# in case of class based view ,we have to call as_view() method
urlpatterns=[
    path("",PostL.as_view(),name="post_l"),
]