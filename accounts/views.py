from django.shortcuts import render

def user_profile(request):
    return render(request, 'accounts/profile.html')


