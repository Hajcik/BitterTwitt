from django.urls import path
from RestAPI import views 
 
urlpatterns = [ 
    path('user',views.user_list_view, name="users"),
    path('user/login',views.login, name="login"),
    path('user/registration',views.user_registration, name="user_registration"),
    path('user/<int:user_id>',views.user_details, name="user_details"),
    path('',views.index),
]