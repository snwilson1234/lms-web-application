from django.shortcuts import render
from account.models import StudentAccount

# Create your views here.

def home_screen_view(request):
    context = {}

    users = StudentAccount.objects.all()
    context['users'] = users
    
    return render(request, "home/home.html", context)
