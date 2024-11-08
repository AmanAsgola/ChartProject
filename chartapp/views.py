from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Dummy data for chart
CHART_DATA = {
    'labels': ["January", "February", "March", "April", "May"],
    'values': [10, 20, 30, 40, 50]
}

# Web Login View
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("chart")
        else:
            return render(request, "chartapp/login.html", {"error": "Invalid credentials"})
    return render(request, "chartapp/login.html")

# Chart View
@login_required
def chart_view(request):
    return render(request, "chartapp/chart.html", {"chart_data": CHART_DATA})

# Chart Data API View
class ChartDataAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(CHART_DATA)
