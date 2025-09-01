from rest_framework import serializers
from .models import Employee, WorkSchedule


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ["id", "name", "email", "position", "department", "start_date"]

    def validate_email(self, value):
        if Employee.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email đã tồn tại.")
        return value


class WorkScheduleUpsertSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField()
    work_day = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d"])
    shift = serializers.ChoiceField(choices=WorkSchedule.Shift.choices)

    def create(self, validated_data):
        employee_id = validated_data["employee_id"]
        work_day = validated_data["work_day"]
        shift = validated_data["shift"]

        try:
            schedule = WorkSchedule.objects.get(employee_id=employee_id, work_day=work_day)
            schedule.shift = shift
            schedule.save(update_fields=["shift"])
            action = "updated"
        except WorkSchedule.DoesNotExist:
            schedule = WorkSchedule.objects.create(**validated_data)
            action = "created"

        return schedule, action