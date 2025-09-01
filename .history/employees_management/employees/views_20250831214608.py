from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer, WorkScheduleUpsertSerializer


from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from .models import Employee
from .serializers import EmployeeSerializer, WorkScheduleUpsertSerializer


# Bài 1 + 2: POST tạo nhân viên mới; GET danh sách theo phòng ban, có lọc & phân trang
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all().order_by("id")
    serializer_class = EmployeeSerializer


    def get_queryset(self):
        qs = super().get_queryset()
        department = self.request.query_params.get("department")
        position = self.request.query_params.get("position")
        name_or_email = self.request.query_params.get("q")
        start_date_gte = self.request.query_params.get("start_date_gte") # YYYY-MM-DD


        if department:
            qs = qs.filter(department__iexact=department)
        if position:
            qs = qs.filter(position__icontains=position)
        if name_or_email:
            qs = qs.filter(Q(name__icontains=name_or_email) | Q(email__icontains=name_or_email))
        if start_date_gte:
            qs = qs.filter(start_date__gte=start_date_gte)
        return qs


# Bài 3: Upsert ca làm việc
class WorkScheduleUpsertView(APIView):
    def post(self, request):
        serializer = WorkScheduleUpsertSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        schedule, action = serializer.save()
        message = "Đã cập nhật" if action == "updated" else "Đã thêm mới"
        return Response({
        "message": message,
        "data": {
        "employee_id": schedule.employee_id,
        "work_day": schedule.work_day,
        "shift": schedule.shift,
        },
        }, status=status.HTTP_200_OK)