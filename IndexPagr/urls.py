from django.urls import path
from . import views

urlpatterns=[
    path('',views.Index,name='indexPage'),
    path('login/',views.Login,name='loginPage'),
    path('register/',views.Register,name='registerPage'),
]