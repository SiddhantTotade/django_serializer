from django.urls import path
from .views import planDeatilView, planView

urlpatterns = [
    path('plan/', planView),
    path('plan/<int:pk>', planDeatilView),
]