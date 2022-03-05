from django.urls import path,include
from event.views import event_view,event_details,add_money,payment_view,add_money_gateway
urlpatterns = [
    path('',event_view,name='event_view'),
    path('<int:id>/',event_details,name='event_details'), 
    path('<int:id>/add_money/',add_money,name='add_money'),
    path('<int:id>/<int:money>/add_money/',add_money_gateway,name='add_money_gateway'),
    path('payment/<int:id>/',payment_view,name='payment'),
]