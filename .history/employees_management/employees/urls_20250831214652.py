from django.urls import path
from .views import EmployeeListCreateView, WorkScheduleUpsertView

urlpatterns = [
    path("employees/", EmployeeListCreateView.as_view(), name="employees-list-create"),
    path("work-schedules/upsert/", WorkScheduleUpsertView.as_view(), name="work-schedule-upsert"),
]