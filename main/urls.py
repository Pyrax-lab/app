"""
urls.py in main 
нужен для того чтобы сортировать ссылки по категориям

"""


from django.urls import path

from main import views

app_name = "main"  # Потдверждает что это имя пространств main

urlpatterns = [
    path('',views.index, name = "index"),
    path('about/', views.about, name ="about"),
    path('contact/', views.contact, name = "contact")
]
