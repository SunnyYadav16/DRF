from django.urls import path, include
from .views import courseview, courseDetailView

urlpatterns = [
    path('', courseview, name='courseview'),
    path('viewdetailcourses/<int:pk>', courseDetailView, name='detailView'),
]
