from django.urls import path
from . import views 
urlpatterns = [
    path('',views.login_,name='login_'),
    path('reg_',views.reg,name='register'),
    path('logout_',views.logout_,name='logout_'),
    path('profile',views.profile,name='profile'),

]
