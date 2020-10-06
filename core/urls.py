from .views import onHomeView
from django.urls import path

urlpatterns = [
    path('', onHomeView.as_view()),
]
