from django.urls import path
from app_1 import views


urlpatterns = [
    path('index/', views.index),    
    path('index2/', views.index2, name='index2'),
    path('index/profile/', views.user_profile),
    # path('index2/', views.index2),    
    # path('index3/', views.index3),    
]
