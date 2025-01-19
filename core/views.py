from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, welcome to the ExcelLocalizer!")


