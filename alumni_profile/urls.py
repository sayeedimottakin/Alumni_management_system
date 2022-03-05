from django.contrib import admin
from django.urls import path,include
from alumni_profile.views import profile_view,create_profile,process_create_profile,profile_update
urlpatterns = [
    path('<int:user_id>/',profile_view,name='alumni_profile'),
    path('<int:user_id>/create_profile/',create_profile,name='create_profile'),
    path('<int:user_id>/create_profile/processs',process_create_profile,name='process_create_profile'),
    path('<int:user_id>/update_profile/',profile_update,name='profile_update'),
]
