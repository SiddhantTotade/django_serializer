from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.views import View
from django.shortcuts import render
from .models import Plan
from .serializer import PlansSerializer

# Create your views here.

# Get and Post API for storing JSON
@api_view(['GET', 'POST'])
def planView(request):
    if request.method == "GET":
        plans = Plan.objects.all()
        print("run")
        plansSerializer = PlansSerializer(plans, many=True)
        return Response(plansSerializer.data)
    elif request.method == "POST":
        plansSerializer = PlansSerializer(data=request.data)
        if plansSerializer.is_valid():
            plansSerializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(plansSerializer.errors)

# Get Put Post Delete API's for JSON and Database operations
@api_view(['GET', 'PUT', 'POST', 'DELETE'])
def planDeatilView(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        planSerializer = PlansSerializer(plan)
        return Response(planSerializer)
    elif request.method == "PUT":
        planSerializer = PlansSerializer(plan, data=request.data)
        if planSerializer.is_valid():
            planSerializer.save()
            return Response(planSerializer.data)
        return Response(planSerializer.errors)
    elif request.method == 'DELETE':
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Getting Plans form Database
class PlanScrapper(View):

    def get(self, request):
        plan = Plan.objects.all()
        return render(request, 'plan_scrapper_app/base.html', {'plan': plan})