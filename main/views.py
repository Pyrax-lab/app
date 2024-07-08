from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories

#Контролеры (функции с request)
def index(request):

    categ = Categories.objects.all()

    context = {
    "title": "Магаз",
    "about": "Магазин мебели и какашак",
    "category": categ}

    return render(request, "main/index.html", context)

def about(request):
    
    context_about = {
        "title_about": "Про нас",
        "about_about": "Мы являемся интернет магазином написаным на фраемворке Django!",
        "text": "Django позволяет нам создавать красивые сайты и что самое важно очень быстро и легко!!"            
          }

    return render(request, "main/about.html", context_about)

def contact(request):

    context_contact = {
        "title_contact": "Контакты",
        "about_contact": "Cвязатся с нами можно с 8:00 - 20:00, по поводу доставки заходите в раздел выше там вся нужная информация. Мы доставляем только в пределах нашего города!"
    }
    return render(request, "main/contact.html", context_contact)