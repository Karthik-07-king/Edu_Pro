from rest_framework import serializers
from edu_core.build.view_environments.all_assignments_course.assignments_of_course.responses.Status_200.Status_200.Status_200Child.Status_200ChildSerializer import Status_200ChildSerializer

class Status_200Serializer(serializers.ListSerializer):
    child = Status_200ChildSerializer()
