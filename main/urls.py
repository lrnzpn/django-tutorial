from django.urls import path
from . import views

urlpatterns = [
    path("<int:id>", views.index, name='index'),  # /1
    path("", views.home, name='home'),  # /
    path("v1/", views.v1, name='v1'),
    path("create/",views.create,name='create'),
    path("view/",views.view,name='view')
]
