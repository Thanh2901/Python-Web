from django.urls import path
from . import views

urlpatterns = [
    path("employees/", views.EmployeeListCreateView, name="employees-list-create"),
    path("work-schedules/upsert/", views.WorkScheduleUpdateOrInsertView, name="work-schedule-upsert"),
]