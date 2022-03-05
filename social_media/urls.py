from django.contrib import admin
from django.urls import path,include
from social_media.views import welcome_view,social_media_view,add_comment,delete_post,post_details,delete_comment,edit_comment
urlpatterns = [
    path('',welcome_view,name='welcome_view'),
    path('posts/',social_media_view,name='social_media_view'),
    path('posts/<int:id>/comment/',add_comment,name='add_comment'),
    path('posts/<int:id>/details/',post_details,name='post_details'),
    path('posts/<int:id>/delete/',delete_post,name='delete_post'),
    path('comment/<int:id>/edit/',edit_comment,name='edit_comment'),
    path('posts/<int:id>/delete_comment/',delete_comment,name='delete_comment'),
]