from rest_framework import serializers
from .models import People,Department

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length = 50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

    def validate(self, data):
        special_char = '!@#$%^&*()+=-}{|\][;"?></.,' 
        if any(c in special_char for c in data['username']):
            raise serializers.ValidationError('Invalid username combination')
        return data

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['department','tutor']

class PeopleSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    class Meta :
        model = People
        fields = '__all__' 
    
    def validate(self,data):
         special_char = '!@#$%^&*()+_-=?><,.;:'
         if any (c in special_char for c in data['name']):
             raise serializers.ValidationError('Name contains special charecters')
         if data['age']<18:
             raise serializers.ValidationError("Age should be 18+")
         
         return data