from django.shortcuts import render,redirect,get_object_or_404
from alumni_profile.models import Alumni_Profile
from alumni_fee.models import Alumni_Fee,Fee_Info,Alumni_Yearly_Fee
from event.models import Event,Contributer
from event.forms import CreateEventForm
from .forms import AdminFeeForm
from .models import My_Admin_Panel
from alumni_management_system.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from news.models import News,News_Letter
from news.forms import NewsFormAdmin,NewsLetterForm

def my_admin_view(request):
    query = get_object_or_404(My_Admin_Panel,admin=request.user)
    people_list = Alumni_Profile.objects.filter(Q(is_verified=False) & Q(ask_for_update_certificate=False))
    context = {
        'people_list':people_list,
    }
    return render(request,"my_admin/my_admin_view.html",context)

def admin_operation_accept(request,id):
    profile = Alumni_Profile.objects.get(pk=id)
    profile.is_verified=True
    profile.ask_for_update_certificate=False
    profile.save()

    fee = Fee_Info.objects.get()
    alumni_fee = Alumni_Fee(
        alumni = profile,
        fee_info = fee
    )
    alumni_fee.save()
    yearly_fee = Alumni_Yearly_Fee(
        alumni_fee=alumni_fee,
        year=alumni_fee.created_on.year,
        amount=fee.yearly_fee,
        is_paid=False,
    )
    yearly_fee.save()
    subject = 'Verification of Alumni'
    message = 'Congrats '+str(profile.full_name)+'! Your Verification is done...Enjoy Our Services...'
    recepient = str(profile.user.email)
    send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('my_admin_view')

def admin_operation_update(request,id):
    profile = Alumni_Profile.objects.get(pk=id)
    profile.ask_for_update_certificate=True
    profile.save()
    subject = 'Verification of Alumni'
    message = request.POST['message']
    # message = 'Warning '+str(profile.full_name)+'! We have found a problem in your certificate.Please Update your certicate.'
    recepient = str(profile.user.email)
    send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('my_admin_view')


def admin_operation_reject(request,id):
    profile = Alumni_Profile.objects.get(pk=id)
    profile.delete()
    subject = 'Verification of Alumni'
    message = request.POST['message']
    # message = 'Sorry '+str(profile.full_name)+'! Your Verification is rejected.'
    recepient = str(profile.user.email)
    send_mail(subject,message, EMAIL_HOST_USER, [recepient], fail_silently = False)
    return redirect('my_admin_view')


def admin_event_view(request):
    query = get_object_or_404(My_Admin_Panel,admin=request.user)
    present_events = Event.objects.filter(Q(is_present=True) & Q(visible_to=''))
    previous_events = Event.objects.filter(Q(is_present=False) & Q(visible_to=''))
    dis_present = Event.objects.filter(Q(is_present=True) & Q(visible_to=request.user.alumni.discipline))
    dis_prev = Event.objects.filter(Q(is_present=False) & Q(visible_to=request.user.alumni.discipline))
    
    form = CreateEventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_event_view')

    context = {
        'events':present_events.union(dis_present),
        'past':previous_events.union(dis_prev),
        'form':form,
    }
    return render(request,"my_admin/my_admin_event_view.html",context)


def admin_event_view_details(request,id):
    event = Event.objects.get(pk=id)
    cont = Contributer.objects.filter(event_no=event)
    context = {
        'event':event,
        'contributers':cont,
    }
    return render(request,'my_admin/my_admin_event_view_details.html',context)


def admin_event_view_edit(request,id):
    event = get_object_or_404(Event,pk=id)
    form = CreateEventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('admin_event_details', id=id)
    context = {
        "form": form
    }
    return render(request, "my_admin/my_admin_event_view_edit.html", context)


def admin_event_view_delete(request,id):
    event = get_object_or_404(Event,pk=id)
    event.delete()
    return redirect('admin_event_view')


def admin_fee_view(request):
    fee = Fee_Info.objects.get()
    form = AdminFeeForm(request.POST or None,instance=fee)
    if form.is_valid():
        form.save()
        return redirect('admin_fee_view')
    todays_date = timezone.now()
    all_fee = Alumni_Fee.objects.all()
    for x in all_fee:
        temp = Alumni_Yearly_Fee.objects.filter(Q(alumni_fee=x) & Q(year=todays_date.year))
        if not temp and x.life_time_fee == 0:
            # print('yooo')
            ayf = Alumni_Yearly_Fee(
                alumni_fee=x,
                year=todays_date.year,
                amount=fee_info.yearly_fee,
                is_paid=False,
            )
            ayf.save() 
    # for x in all_fee:
    #     # start = x.created_on.date()
    #     # days = x.yearly_fee_count*365
    #     # end = start+timedelta(days=days)
    #     todays_date = timezone.now()
    #     # print(todays_date.date() >= end)
    #     # if todays_date.date() >= end:
    #     #     x.yearly_fee = 0
    #     #     x.save()
    #     if todays_date
    alumni_fee = Alumni_Fee.objects.exclude(registration_fee=fee.registration_fee)
    yearly_fee = Alumni_Yearly_Fee.objects.filter(is_paid=False)
    context = {
        'fee':fee,
        'form':form,
        'alumni_fee':alumni_fee,
        'yearly_fee':yearly_fee,
    }
    return render(request,"my_admin/my_admin_fee_view.html",context)


def send_notification_reg_fee(request):
    subject = 'Due of Registration Fee'
    message = request.POST['message']
    # print(message)
    alumnis = request.POST.getlist('alumni_name')
    #print(alumnis)
    recepient = []
    for x in alumnis:
        user = User.objects.get(id=x)
        recepient.append(str(user.email))
    print(recepient)    
    send_mail(subject,message, EMAIL_HOST_USER, recepient, fail_silently = False)
    return redirect('admin_fee_view')


def send_notification_yearly_fee(request):
    subject = 'Due of Yearly Fee'
    message = request.POST['message']
    # print(message)
    alumnis = request.POST.getlist('alumni_name1')
    # print(alumnis)
    recepient = []
    for x in alumnis:
        user = User.objects.get(id=x)
        recepient.append(str(user.email))
        
    send_mail(subject,message, EMAIL_HOST_USER, recepient, fail_silently = False)
    return redirect('admin_fee_view')


def my_admin_news_view(request):
    news_letter = News_Letter.objects.all().order_by('-start_date')
    pending_news = News.objects.filter(is_approved=False)
    all_news = News.objects.filter(is_approved=True)
    news_form = NewsFormAdmin(request.POST or None)
    news_letter_form = NewsLetterForm(request.POST or None)
    if news_letter_form.is_valid():
        new_letter = news_letter_form.save()
        return redirect('admin_news_view')
    if news_form.is_valid():
        new_news = news_form.save(commit=False)
        new_news.is_approved = True
        new_news.author = request.user.alumni
        new_news.save()
        news_form.save_m2m()
        return redirect('admin_news_view')
    context = {
        'pending_news':pending_news,
        'news_form':news_form,
        'all_news':all_news,
        'news_letter_form':news_letter_form,
        'news_letter':news_letter,
    }
    return render(request,"my_admin/my_admin_news_view.html",context)

def admin_news_letter_update(request,id):
    news_letter = News_Letter.objects.get(pk=id)
    form = NewsLetterForm(request.POST or None, instance=news_letter)
    if form.is_valid():
        form.save()
        return redirect('admin_news_view')
    context = {
        'news_letter':news_letter,
        'form':form,
    }
    return render(request,"my_admin/my_admin_update_news_letter.html",context)

def admin_news_upadte(request,id):
    news = News.objects.get(pk=id)
    news_form = NewsFormAdmin(request.POST or None, instance=news)
    if news_form.is_valid():
        news_form.save()
        return redirect('admin_news_view')
    context = {
        'news':news,
        'form':news_form,
    }
    return render(request,"my_admin/admin_update_news.html",context)


def my_admin_news_delete(request,id):
    news = News.objects.get(pk=id)
    news.delete()
    return redirect('admin_news_view')

def my_admin_news_letter_delete(request,id):
    news_letter = News_Letter.objects.get(pk=id)
    news_letter.delete()
    return redirect('admin_news_view')

def my_admin_news_approve(request,id):
    news = News.objects.get(pk=id)
    news.is_approved = True
    news.save()
    return redirect('admin_news_view')
    




    

    