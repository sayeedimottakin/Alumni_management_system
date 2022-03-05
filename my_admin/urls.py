from django.urls import path,include
from my_admin.views import my_admin_view,admin_operation_accept,admin_operation_reject,admin_operation_update,admin_event_view,admin_event_view_details,admin_event_view_edit,admin_event_view_delete,admin_fee_view,send_notification_reg_fee,send_notification_yearly_fee,my_admin_news_view,admin_news_upadte,my_admin_news_delete,my_admin_news_approve,admin_news_letter_update,my_admin_news_letter_delete

urlpatterns = [
    path('',my_admin_view,name='my_admin_view'),
    path('<int:id>/admin_operation/accept/',admin_operation_accept,name='admin_operation_accept'),
    path('<int:id>/admin_operation/reject/',admin_operation_reject,name='admin_operation_reject'),
    path('<int:id>/admin_operation/update/',admin_operation_update,name='admin_operation_update'),
    path('event_view/',admin_event_view,name='admin_event_view'),
    path('event_view/<int:id>/details/',admin_event_view_details,name='admin_event_details'),
    path('event_view/<int:id>/edit/',admin_event_view_edit,name='admin_event_edit'),
    path('event_view/<int:id>/delete/',admin_event_view_delete,name='admin_event_delete'),
    path('fee_view/',admin_fee_view,name='admin_fee_view'),
    path('send_notication_reg_fee/',send_notification_reg_fee,name='send_notification_reg_fee'),
    path('send_notication_yearly_fee/',send_notification_yearly_fee,name='send_notification_yearly_fee'),
    path('news_view/',my_admin_news_view,name='admin_news_view'),
    path('news_view/<int:id>/update/',admin_news_upadte,name='admin_news_update'),
    path('news_view/<int:id>/delete/',my_admin_news_delete,name='admin_news_delete'),
    path('news_view/<int:id>/approve/',my_admin_news_approve,name='admin_news_approve'),
    path('news_view/<int:id>/newsletter/update/',admin_news_letter_update,name='admin_news_letter_update'),
    path('news_view/<int:id>/newsletter/delete/',my_admin_news_letter_delete,name='admin_news_letter_delete'),
]
    