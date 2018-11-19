from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ProfileForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        user_form = SignUpForm(request.POST)
        profile_form= ProfileForm(request.POST, request.FILES)
        # request.FILES allows us to attach image
        
        if user_form.is_valid() and profile_form.is_valid():
            
            user=user_form.save()
            # save user to database
            profile=profile_form.save(commit=False)
            # dont save profile
            profile.user=user
            # set profile user to user
            profile.save()
            # finally save profile
            
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('get_index')
    else:
        user_form = SignUpForm()
        profile_form = ProfileForm()
    return render(request, 'registration/signup.html', {'user_form': user_form, 'profile_form': profile_form})
    
    
def show_profile(request):
    return render(request, 'profile.html')