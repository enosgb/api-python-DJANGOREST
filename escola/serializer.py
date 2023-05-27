from calendar import c
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from escola.models import Student,Course,Registration

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','rg','cpf','birth_date']    

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
    def to_representation(self, instance):    
        rep = super(CourseSerializer, self).to_representation(instance)        
        rep['level_name'] = instance.get_level_display()        
        return rep
    

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"
    def to_representation(self, instance):    
        rep = super(RegistrationSerializer, self).to_representation(instance)        
        rep['course_name'] = instance.course.description
        rep['student_name'] = instance.student.name   
        rep["period_name"] = instance.get_period_display()  
        return rep
   

class ListRegistrationStudentsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Registration
        fields = ['course', 'period']
    def get_period(self,obj):
        return obj.get_periodo_display()

class ListaRegistrationsStudentsSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Registration
        fields = ['student_name']


class ListCourseLevelsSerializer(serializers.Serializer):
    value = serializers.CharField()
    option = serializers.CharField()

class ListRegistrationPeriodSerializer(serializers.Serializer):
    value = serializers.CharField()
    option = serializers.CharField()

