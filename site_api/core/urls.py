from django.urls import path
from . import views

urlpatterns = {
    
    path('all_users', views.all_users, name='all_users'),
    path('all_quotes', views.all_quotes, name='all_quotes'),
}