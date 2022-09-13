from django.urls import path
from .views import planDeatilView, planView, PlanScrapper

urlpatterns = [
    path('plan/', planView),
    path('plan/<int:pk>', planDeatilView),
    path('plan-list', PlanScrapper.as_view())
]