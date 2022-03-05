from django.urls import path,include
from .views import news_letter_view,news_details,news_search_result
urlpatterns = [
    path('<int:id>/',news_letter_view,name='news_view'),
    path('news/<int:id>/details/',news_details,name='news_details'),
    path('search_results/',news_search_result,name='news_search_result'),
]