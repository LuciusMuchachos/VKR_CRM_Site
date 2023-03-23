from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile

@login_required
def profile(request):
    context = {"Profile": Profile.objects.all()}
    return render(request, "users/profile.html", context)