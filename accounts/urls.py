
from django.urls import path
from . import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('register/',views.register,name='register'),
    path('login/', views.login,name='login'),
    path('index/', views.index,name='index'),
    path('logout/', views.logout,name='logout'),
    path('',views.main,name='main'),
    path('delete/',views.delete,name='delete'),

]
