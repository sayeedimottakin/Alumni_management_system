from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from alumni_profile.models import Alumni_Profile
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q
# Create your views here.
@login_required
def search_view(request):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home')  

    disciplines= list(set(Alumni_Profile.objects.values_list('discipline',flat=True).filter(is_verified=True)))
    disciplines.sort()
    disciplines.insert(0,'All')
    
    batch = list(set(Alumni_Profile.objects.values_list('batch',flat=True).filter(is_verified=True)))
    batch.sort()
    batch.insert(0,'All')
    Ids = ['All']

    for x in range(1,51):
        Ids.append(x)

    country = list(set(Alumni_Profile.objects.values_list('present_country',flat=True).filter(is_verified=True)))
    country.sort()
    country.insert(0,'All')

    context={
        'disciplines':disciplines,
        'batch':batch,
        # 'Ids':Ids,
        'country':country,
    }
    return render(request,"search/search_view.html",context)

@login_required
def search_result(request):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home') 
   
    discipline = request.POST['discipline']
    batch = request.POST['batch']
    # student_id = request.POST['id']
    country = request.POST['country']

    my_dict = {
        'discipline':discipline,
        'batch':batch,
        # 'student_id':student_id,
        'present_country':country,
    }
    
    final_query = Alumni_Profile.objects.filter(is_verified=True)
    for x in my_dict:
        if my_dict[x]!='All':
            query = Alumni_Profile.objects.filter(**{x: my_dict[x]})
            final_query = final_query.intersection(query)
        else:
            pass
    # print(final_query)
    context={
        'profiles':final_query,
    }
    return render(request,"search/search_result.html",context)

@login_required
def search_result_details(request,id):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home') 
    
    query = Alumni_Profile.objects.get(pk=id)
    context = {
        'profile':query,
    }

    return render(request,"search/search_result_details.html",context)
    

def advance_search_results(request):
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)   
    except:
        pass
    if not profile or profile.is_verified == False:
        return redirect('home')

    field_list = ['full_name','discipline','batch','student_id','job_type','job_position','higher_study','present_address','present_country','prmanent_address']

    value = request.POST['search']
    context = {}


    if value:
        for x in field_list:
            field_column = x
            st = field_column + '__icontains'
            query = Alumni_Profile.objects.filter(Q(**{st:value}) & Q(is_verified=True))
            
            if query.exists():
                context[field_column]=query
            else:
                pass
    else:
        pass

    return render(request,"search/advance_search_result.html",{'context':context})






