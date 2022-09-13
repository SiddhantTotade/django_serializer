from cgitb import reset
from lib2to3.pgen2 import driver
from urllib import request
from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Plan
from .serializer import PlansSerializer
# Create your views here.


@api_view(['GET', 'POST'])
def planView(request):
    if request.method == "GET":
        plans = Plan.objects.all()
        plansSerializer = PlansSerializer(plans, many=True)
        return Response(plansSerializer.data)
    elif request.method == "POST":
        plansSerializer = PlansSerializer(data=request.data)
        if plansSerializer.is_valid():
            plansSerializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(plansSerializer.errors)


@api_view(['GET', 'PUT', 'POST'])
def planDeatilView(request, pk):
    try:
        plan = Plan.objects.get(pk=pk)
    except Plan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return Response(plan)
    elif request.method == "PUT":
        planserializer = PlansSerializer(plan, data=request.data)
        if planserializer.is_valid():
            planserializer.save()
            return Response(planserializer.data)
        return Response(planserializer.errors)
    elif request.method == 'DELETE':
        plan.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# def scrapper():
#     driver = webdriver.Chrome("/usr/bin/chromedriver")
#     driver.get("https://www.airtel.in/myplan-infinity/")

#     monthly_rental_price = driver.find_elements(By.CLASS_NAME, "price")
#     data_with_rollover = driver.find_elements(By.CLASS_NAME,'')