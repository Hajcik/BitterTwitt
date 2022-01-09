from django.urls import path
from RestAPI import views 
 
urlpatterns = [ 
    path('user',views.user_list_view, name="users"),
    path('user/registration',views.user_registration, name="user_registration"),
    path('',views.index),
]