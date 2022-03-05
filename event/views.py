from django.shortcuts import render,redirect
from .models import Event,Contributer
from django.db.models import Q
from sslcommerz_lib import SSLCOMMERZ
from django.utils import timezone
from datetime import datetime,timedelta
# from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.
def event_view(request):
    present_events = Event.objects.filter(Q(is_present=True) & Q(visible_to=''))
    previous_events = Event.objects.filter(Q(is_present=False) & Q(visible_to=''))
    dis_present = Event.objects.filter(Q(is_present=True) & Q(visible_to=request.user.alumni.discipline))
    dis_prev = Event.objects.filter(Q(is_present=False) & Q(visible_to=request.user.alumni.discipline))
    # print(dis_prev)

    # start_date = datetime.strptime('10/23/2020','%m/%d/%Y')
    # end_date = datetime.strptime('12/31/2020','%m/%d/%Y')
    # weekly = Contributer.objects.filter(created_on__date__range=[start_date.date(), end_date.date()])
    # # weekly = Contributer.objects.filter(created_on__date = end_date.date())
    # for i in weekly:
    #     print(i.created_on)

    context = {
        'events':present_events.union(dis_present),
        'past':previous_events.union(dis_prev),
    }
    return render(request,'event/event_view.html',context)


def event_details(request,id):
    # print(datetime.datetime.now())
    # print(timezone.now())
    event = Event.objects.get(pk=id)
    cont = Contributer.objects.filter(event_no=event).order_by('-created_on')
    # print(cont)
    context = {
        'event':event,
        'contributers':cont,
    }
    return render(request,'event/event_details.html',context)


def add_money(request,id):
    amount = int(request.POST['amount'])
    event = Event.objects.get(pk=id)
    if amount:
        contributer = Contributer(
            alumni=request.user.alumni,
            event_no= event,
            amount=amount,
        )
        contributer.save()
        temp =event.present_amount = event.present_amount + amount
        event.save()
        return redirect('event_details', id=id)


def add_money_gateway(request,id,money):
    event = Event.objects.get(pk=id)
    if money:
        contributer = Contributer(
            alumni=request.user.alumni,
            event_no= event,
            amount=money,
            created_on=datetime.now(),
        )
        contributer.save()
        temp =event.present_amount = event.present_amount + money
        event.save()
        return redirect('event_details', id=id)

# @csrf_exempt
def payment_view(request,id):
    amount = request.POST['amount']
    transaction_id = str(id)+'alumni_system'+str(request.user.id)
    if request.method == "POST":
        settings = { 'store_id': 'khuln5fec00df28f87', 'store_pass': 'khuln5fec00df28f87@ssl', 'issandbox': True }
        sslcommez = SSLCOMMERZ(settings)
        post_body = {}
        post_body['total_amount'] = amount
        post_body['currency'] = "BDT"
        post_body['tran_id'] = transaction_id
        post_body['success_url'] = "http://127.0.0.1:8000/success_payment/"
        post_body['fail_url'] = "your fail url"
        post_body['cancel_url'] = "your cancel url"
        post_body['emi_option'] = 0
        post_body['cus_name'] = "test"
        post_body['cus_email'] = "test@test.com"
        post_body['cus_phone'] = "01700000000"
        post_body['cus_add1'] = "customer address"
        post_body['cus_city'] = "Dhaka"
        post_body['cus_country'] = "Bangladesh"
        post_body['shipping_method'] = "NO"
        post_body['multi_card_name'] = ""
        post_body['num_of_item'] = 1
        post_body['product_name'] = "Test"
        post_body['product_category'] = "Test Category"
        post_body['product_profile'] = "general"

        response = sslcommez.createSession(post_body)
        # print(response)
        payment_url = response['GatewayPageURL']
        return redirect(payment_url)


    
