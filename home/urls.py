from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
#path('', views.home, name = 'home'),
path('', views.upload, name = 'homepage'),
path('logout', views.sign_out, name="signout"),
path('contacts', views.contacts, name="contacts"),
path('departement_GIT', views.departement_GIT, name="departement_GIT"),
path('basic/', views.API_objects.as_view()),
path('basic/<int:pk>/', views.API_objects_details.as_view()),
path('departement_CIVIL', views.departement_GIT, name="departement_GIT"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
