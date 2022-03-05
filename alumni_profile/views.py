from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UpdateProfileForm
from .models import Alumni_Profile
# Create your views here.
@login_required
def profile_view(request,user_id):
    hasProfile = False
    profile = []
    try:
        profile = Alumni_Profile.objects.get(user=request.user)
        hasProfile = True
    except:
        pass
    # print(hasProfile)
    context={
        'hasProfile':hasProfile,
        'profile':profile,
    }
    return render(request,"profile/profile_view.html",context)

@login_required
def create_profile(request,user_id):
    form = ProfileForm()
    context={
        'form':form,
    }
    return render(request,"profile/create_profile.html",context)

def process_create_profile(request,user_id):
    form = ProfileForm()
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        # print(form.errors)
        if form.is_valid():
            profile = Alumni_Profile(
                full_name=form.cleaned_data["full_name"],
                image=form.cleaned_data["profile_pic"],
                certificate=form.cleaned_data["certificate"],
                discipline=form.cleaned_data["discipline"],
                student_id=form.cleaned_data["student_id"],
                batch=form.cleaned_data["batch"],
                job_type=form.cleaned_data["job_type"],
                job_position=form.cleaned_data["job_posi"],
                higher_study=form.cleaned_data["higher_study"],
                present_address=form.cleaned_data["present_address"],
                present_country=form.cleaned_data["present_country"],
                prmanent_address=form.cleaned_data["parmanent_address"],
                mobile=form.cleaned_data["mobile"],
                facebook = form.cleaned_data["facebook"],
                linkdin=form.cleaned_data["linkdin"],
                about_me=form.cleaned_data["about_me"],
                user=request.user,
            )
            # print(profile)
            profile.save()
            return redirect('home')
    context = {}
    return render(request,"profile/profile_view.html",context)

@login_required
def profile_update(request, user_id):
    profile = get_object_or_404(Alumni_Profile, user=request.user)
    form = UpdateProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        profile.ask_for_update_certificate = False
        profile.save()
        return redirect('alumni_profile', user_id=user_id)
    context = {
        "form": form
    }
    return render(request, "profile/update_profile.html", context)