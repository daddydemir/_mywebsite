from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('users/' , views.get_users , name="users"),
    path('users/add' , views.add_user , name="add_user"),
    path('users/detail/<int:pk>/' , views.get_user , name="user"),

]