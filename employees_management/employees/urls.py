from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.EmployeeListCreateView.as_view(), name="employees-list-create"),
    path("work-schedules/upsert/", views.WorkScheduleUpdateOrInsertView.as_view(), name="work-schedule-upsert"),
]