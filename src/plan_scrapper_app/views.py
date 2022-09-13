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
        print("run")
        plansSerializer = PlansSerializer(plans, many=True)
        return Response(plansSerializer.data)
    elif request.method == "POST":
        plansSerializer = PlansSerializer(data=request.data)
        if plansSerializer.is_valid():
            plansSerializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(plansSerializer.errors)


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


# def scrapper():
#     driver = webdriver.Chrome("/usr/bin/chromedriver")
#     driver.get("https://www.airtel.in/myplan-infinity/")

#     monthly_rental_price = driver.find_elements(By.CLASS_NAME, "price")
#     data_with_rollover = driver.find_elements(By.CLASS_NAME,'')