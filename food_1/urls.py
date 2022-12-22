from django.urls import path
from food_1 import views

urlpatterns=[
    path('food/',views.Snippetlist.as_view()),

    path('food/<int:pk>/',views.Snippetdetails.as_view())
    
]