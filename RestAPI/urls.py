from django.urls import path
from RestAPI import views 
 
urlpatterns = [ 
    path('users-view',views.user_list_view),
    path('users',views.user_list),
    path('user-registration',views.user_registration),
    path('',views.index)
]