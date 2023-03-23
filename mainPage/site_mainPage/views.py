from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import order_Card

def mainPage(request):
    return render(request,"mainPage/mainPage.html")

@login_required
def kanban_desk(request):
    context = {
        "work_name": ["Программирование", "Дизайн", "SMM-менеджмент", "Реклама", "Пиво", "Чебупели"],
    }
    # return response
    return render(request, "kanban_desk/kanban_desk.html", context)

@login_required
def order_card(request):
    return render(request, "order_Card/order_card.html")

@login_required
def account_list(request):
    return render(request, "program_settings/account_settings/account_list.html")

