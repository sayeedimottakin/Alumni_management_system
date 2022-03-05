from django.contrib import admin
from django.urls import path,include
from search.views import search_view,search_result,search_result_details,advance_search_results
urlpatterns = [
    path('',search_view,name='search_view'),
    path('search_result/',search_result,name='search_result'),
    path('search_result_details/<int:id>/',search_result_details,name='search_result_details'),
    # path('ajax_search/',ajax_search_results,name='ajax_search_results'),
    path('advance_search_result/',advance_search_results,name='advance_search_result')
]