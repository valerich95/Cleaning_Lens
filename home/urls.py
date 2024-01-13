from django.urls import path
from . import views


urlpatterns = [
    path('' , views.HomeView.as_view() ),
    path('calculate/', views.CleaningPriceView.as_view())
]
