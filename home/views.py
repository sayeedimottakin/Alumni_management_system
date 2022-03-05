from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from alumni_profile.models import Alumni_Profile
from django.db.models import Q
from event.models import Event
from news.models import News,News_Letter

discipline_dict = {
    'Architecture':'Architecture',
    'CSE':'Computer Science & Engineering',
    'ECE':'Electronics and Communication Engineering',
    'Math':'Mathematics',
    'URP':'Urban and Rural Planning',
    'Physics':'Physics',
    'Chemistry':'Chemistry',
    'Stat':'Statistics',
    'Pharmacy':'Pharmacy',
    'BGE':'Biotechnology & Genetic Engineering',
    'FWT':'Forestry & Wood Technology',
    'FMRT':'Fisheries & Marine Resources Technology',
    'Agrotechnology':'Agrotechnology',
    'ES':'Environmental Science',
    'SWE':'Soil,Water and Environment',
    'BAD':'Business Administration',
    'HRM':'Human Resource Management',
    'DP':'Drawing and Paininting',
    'PM':'Printmaking',
    'DS':'Development Studies',
    'History':'History and Civilization',
    'English':'English',
    'Bangla':'Bangla',
    'IER':'Institute of Education and Research',
    'Sculpture':'Sculpture',
    'Econ':'Economics',
    'Sociology':'Sociology',
    'MCJ':'Mass Communication & Journalism',
    'Law':'Law and JUstice',
}
# Create your views here.
@login_required
def home_view(request):
    hasProfile = False
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)
        hasProfile = True
    except:
        pass

    news_letter = News_Letter.objects.all().order_by('-start_date').first()
    news_list = news_letter.news.all()[:6]
    news_list_extra = news_letter.news.all()[6:]
    # print(news_letter.news.all())
    # for x in news_letter.news:
    #     print(x)
    context={
        'profile':profile,
        'hasProfile':hasProfile,
        'news_list':news_list,
        'news_letter':news_letter,
        'news_list_extra':news_list_extra,
    }
    return render(request,"home/home_view.html",context)

def discipline_view(request):
    dis = request.user.alumni.discipline
    full_dis = discipline_dict[dis]
    print(full_dis)
    temp = Alumni_Profile.objects.filter(Q(discipline=dis) & Q(is_verified=True))
    batches = []
    for x in temp:
        if x.batch not in batches:
            batches.append(x.batch)

    dis_present = Event.objects.filter(Q(is_present=True) & Q(discipline=request.user.alumni.discipline))
    dis_prev = Event.objects.filter(Q(is_present=False) & Q(discipline=request.user.alumni.discipline))
    return render(request,"home/discipline_view.html",{'batches':batches,'events':dis_present,'past':dis_prev,'full_dis':full_dis})


def discipline_view_search_results(request):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home')
    dis = request.user.alumni.discipline
    full_dis = discipline_dict[dis]
    context = {}
    # print(request.POST['batch'])
    try:
        batch = request.POST['batch']
        people_list = Alumni_Profile.objects.filter(Q(is_verified=True) & Q(batch=batch) & Q(discipline=request.user.alumni.discipline))
        # print(people_list)
        context = {
            'profiles':people_list,
            'full_dis':full_dis,
        }
        return render(request,"home/discipline_view_search_results.html",context)
    except:
        pass

    field_list = ['full_name','batch','student_id','job_type','job_position','higher_study','present_address','present_country','prmanent_address']

    value = request.POST['discipline_advance']
    if value:
        for x in field_list:
            field_column = x
            st = field_column + '__icontains'
            query = Alumni_Profile.objects.filter(Q(**{st:value}) & Q(is_verified=True) & Q(discipline=request.user.alumni.discipline))
            if query.exists():
                context[field_column]=query
            else:
                pass
    else:
        pass
    return render(request,"home/discipline_view_search_results.html",{'context':context,'full_dis':full_dis})


def success_payment(request):
    amount  = request.POST['amount']
    tran_id = request.POST['tran_id']
    print(int(float(amount)))
    print(tran_id[0])
    event_id = int(tran_id[0])
    context = {
        'amount':int(float(amount)),
        'event_id':event_id,
    }
    return render(request,"home/success_payment.html",context)
    
