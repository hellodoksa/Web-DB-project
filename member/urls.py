# member\urls.py

from django.urls import path
from . import views 

urlpatterns = [
    # member
    path('main', views.main),
    path('sign_up', views.sign_up),
    path('sign_in', views.sign_in),
    path('sign_out', views.sign_out),
    path('user_mypage', views.user_mypage),
    path('user_edit', views.user_edit),
    path('user_edit_check', views.user_edit_check),
    path('user_edit_pw', views.user_edit_pw),
    
    
   
    
    
    
    
    

]


# log
# 일단 네임은 생략  

