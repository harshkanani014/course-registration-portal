from rest_framework.relations import SlugRelatedField
from .models import *
from rest_framework import serializers
from accounts.models import User


# superAdmin serializer for saving, editing admin/superadmin
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'registration_number', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
            'id':{'read_only': True}
        }

    def update(self, instance, validated_data):
        if(instance.password):
            for attr, value in validated_data.items():
                if attr == 'password' and value!="null":
                    instance.set_password(value)
                elif attr == 'password' and value=="null":
                    pass
                else:
                    setattr(instance, attr, value)
            instance.save()
            return instance
        else:
            instance.save()
            return instance

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


# course to add and update course
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
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


# class serializer to add and update class
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'
        extra_kwargs = {
            'students_registered': {'read_only': True},
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


# class serializer to get all class details
class GetClassSerializer(serializers.ModelSerializer):
    course_code = serializers.StringRelatedField()
    building = serializers.StringRelatedField()
    class Meta:
        model = Classes
        fields = '__all__'
        extra_kwargs = {
            'id': {'read_only': True},
            'course_code':{'read_only':True},
            'building_name':{'read_only':True},
        }


# Location serializer to add and update location  
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
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