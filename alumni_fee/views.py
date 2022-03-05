from django.shortcuts import render,redirect
from .models import Fee_Info,Alumni_Fee,Alumni_Yearly_Fee
from django.utils import timezone
from datetime import datetime, timedelta
import math
from django.db.models import Q
# Create your views here.
def alumni_fee_home(request,id):
    fee_info = Fee_Info.objects.get()
    alumni_fee = Alumni_Fee.objects.get(alumni=id)
    
    # date1 = datetime.strptime('1/1/2020','%m/%d/%Y')
    # print(timezone.now().date())
    # print(date1.date())
    # print((timezone.now().date()-date1.date()).days)
    # temp = Alumni_Fee.objects.filter(created_on__contains='2020-12-09')
    # print(temp)

    if alumni_fee.life_time_fee == fee_info.life_time_fee:
        alumni_fee.registration_fee = fee_info.registration_fee
        alumni_fee.save()
        yf = Alumni_Yearly_Fee.objects.filter(Q(alumni_fee=alumni_fee) & Q(is_paid=False))
        for x in yf:
            x.is_paid = True
            x.save()

    due = [fee_info.registration_fee-alumni_fee.registration_fee,fee_info.life_time_fee-alumni_fee.life_time_fee]

    todays_date = timezone.now()
    #todays_date = datetime.strptime('3/5/2021','%m/%d/%Y')
    
    expired_yearly_fee_date = ''

    yearly_fees_paid = Alumni_Yearly_Fee.objects.filter(Q(alumni_fee=alumni_fee) & Q(is_paid=True))

    temp = Alumni_Yearly_Fee.objects.filter(Q(alumni_fee=alumni_fee) & Q(year=todays_date.year))
    if not temp and alumni_fee.life_time_fee == 0:
        # print('yooo')
        ayf = Alumni_Yearly_Fee(
            alumni_fee=alumni_fee,
            year=todays_date.year,
            amount=fee_info.yearly_fee,
            is_paid=False,
        )
        ayf.save() 
    # print(yearly_fee)
    # if not yearly_fee:
        
        # print('yooo')
        #year = (todays_date.year-alumni_fee.created_on.year)+1
    # else:
    #     expired_yearly_fee_date = alumni_fee.created_on+timedelta(days=alumni_fee.yearly_fee_count*365)
    #     year = (todays_date.year-expired_yearly_fee_date.year)+1

    yearly_fees = Alumni_Yearly_Fee.objects.filter(Q(alumni_fee=alumni_fee))
    paid_years = []
    for x in yearly_fees:
        paid_years.append(x.year)
    # print(paid_years)
    advance_years = []
    present_year = todays_date.year+1
    for x in range(11):
        if str(present_year+x) in paid_years:
            # print('yoo')
            continue
        else:
            advance_years.append(present_year+x)
    # print(advance_years)
    # year = 3
    # year_fee = year*fee_info.yearly_fee

    return render(request,"fee/fee_home.html",{'fee_info':fee_info,'due':due,'alumni_fee':alumni_fee,'yearly_fees':yearly_fees,'advance_years':advance_years})


def add_money_reg_fee(request,id):
    fee_info = Fee_Info.objects.get()
    alumni_fee = Alumni_Fee.objects.get(alumni=id)
    # money = request.POST['amount']
    alumni_fee.registration_fee = fee_info.registration_fee
    alumni_fee.save()
    return redirect('alumni_fee_home',id=id)


def add_money_yearly_fee(request,id,id1):
    fee_info = Fee_Info.objects.get()
    alumni_fee = Alumni_Fee.objects.get(alumni=id)
    yearly_fee = Alumni_Yearly_Fee.objects.get(id=id1)
    print(yearly_fee.amount)
    yearly_fee.is_paid = True
    yearly_fee.save()
    return redirect('alumni_fee_home',id=id)


def add_money_life_time_fee(request,id):
    fee_info = Fee_Info.objects.get()
    alumni_fee = Alumni_Fee.objects.get(alumni=id)
    # money = request.POST['amount']
    alumni_fee.life_time_fee = fee_info.life_time_fee
    alumni_fee.save()
    return redirect('alumni_fee_home',id=id)

def add_advance_money_yearly_fee(request,id):
    fee_info = Fee_Info.objects.get()
    alumni_fee = Alumni_Fee.objects.get(alumni=id)
    years = request.POST.getlist('advance_year')
    for x in years:
        aayf = Alumni_Yearly_Fee(
            alumni_fee=alumni_fee,
            year=x,
            amount=fee_info.yearly_fee,
            is_paid=True,
        )
        aayf.save()

    return redirect('alumni_fee_home',id=id)

