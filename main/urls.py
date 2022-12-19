from django.urls import path
from . import views


urlpatterns = [
    path('drinks/',views.drink_list, name='drinks'),
    path('drinks/<int:id>/',views.drink_detail, name='drinks-detail'),
]
