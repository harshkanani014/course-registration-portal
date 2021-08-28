from rest_framework.relations import SlugRelatedField
from .models import *
from rest_framework import serializers
from accounts.models import User
from course_coordinator.serializers import GetClassSerializer

class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class GetTimeTableSerializer(serializers.ModelSerializer):
    #student_id = serializers.StringRelatedField()
    class_id = GetClassSerializer()
    class Meta:
        model = TimeTable
        fields = ('id', 'class_id',)
        extra_kwargs = {
            'id': {'read_only': True},
        }