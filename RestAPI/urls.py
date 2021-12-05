from django.urls import path
from RestAPI import views 
 
urlpatterns = [ 
    path('users_view',views.user_list_view),
    path('users',views.user_list),
    path('users/:id',views.user_list),
]