from lib2to3.pgen2 import driver
from urllib import request
from django.shortcuts import render, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your views here.
from .models import Plan


class PlanView(request):
    pass


def scrapper():
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    driver.get("https://www.airtel.in/myplan-infinity/")

    monthly_rental_price = driver.find_elements(By.CLASS_NAME, "price")
    data_with_rollover = driver.find_elements(By.CLASS_NAME,'')