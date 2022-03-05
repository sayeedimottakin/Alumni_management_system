from django.urls import path,include
from home.views import home_view,discipline_view,discipline_view_search_results,success_payment

urlpatterns = [
    path('',home_view,name='home'),
    path('discipline_view/',discipline_view,name='discipline_view'),
    path('discipline_view/search_results/',discipline_view_search_results,name='discipline_view_search_results'),
    path('success_payment/',success_payment,name='success_payment'),
]