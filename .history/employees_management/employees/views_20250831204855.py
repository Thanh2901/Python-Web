from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer, WorkScheduleUpsertSerializer