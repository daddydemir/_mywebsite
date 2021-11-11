from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('users/' , views.get_users , name="users"),
    path('users/add' , views.add_user , name="add_user"),
    path('users/detail/<int:pk>/' , views.get_user , name="user"),
    path('add/post/' , views.add_post , name="add_post"),
    #path('edit/post/<int:pk>/' , views.edit_post , name="edit_post"),

]