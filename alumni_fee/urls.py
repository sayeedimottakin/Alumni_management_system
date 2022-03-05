from django.urls import path,include
from .views import alumni_fee_home,add_money_reg_fee,add_money_life_time_fee,add_money_yearly_fee,add_advance_money_yearly_fee
urlpatterns = [
    path('<int:id>/',alumni_fee_home,name='alumni_fee_home'),
    path('<int:id>/reg_fee/',add_money_reg_fee,name='reg_fee'),
    path('<int:id>/yearly_fee/<int:id1>/',add_money_yearly_fee,name='yearly_fee'),
    path('<int:id>/life_fee/',add_money_life_time_fee,name='life_time_fee'),
    path('<int:id>/advance_yearly_fee/',add_advance_money_yearly_fee,name='advance_yearly_fee'),
]