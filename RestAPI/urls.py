from django.urls import path
from RestAPI import views 
 
urlpatterns = [ 
    path('user',views.user_list_view, name="users"),
    path('login',views.login_view, name="login"),
    path('logout',views.logout_view, name="logout"),
    path('user/registration',views.user_registration, name="user_registration"),
    path('user/<int:user_id>',views.user_details, name="user_details"),
    path('user/<int:user_id>/add_comment',views.postTwitt, name="postTwitt"),
    path('',views.index),
]