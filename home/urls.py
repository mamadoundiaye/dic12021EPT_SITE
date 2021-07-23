from django.urls import path
from . import views
urlpatterns = [
#path('', views.home, name = 'home'),
path('', views.upload, name = 'homepage'),
path('logout', views.sign_out, name="signout"),
]
