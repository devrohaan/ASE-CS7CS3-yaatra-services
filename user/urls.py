from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/', views.user_login),
    url(r'register/', views.user_registration),
    url(r'rating/', views.update_user_rating),
    ]