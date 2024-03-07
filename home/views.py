from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import People
from .serializers import PeopleSerializer,LoginSerializer

@api_view(['GET'])
def index(request):

    if request.method == 'GET':
    
        courses = {
            'c_name':'Python',
            'c_duration':'9 Months',
            'c_subjects':['Django','RestAPI','AWS'],
        }

        return Response(courses)

@api_view(['POST'])
def login(request):
     data = request.data
     serializer = LoginSerializer(data=data)

     if serializer.is_valid():
          return Response({'message':'success login',
                           'logindata':serializer.data})
     return Response(serializer.errors)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def person(request):
     
     if request.method == 'GET':
          obj = People.objects.all()
          serializer = PeopleSerializer(obj , many = True)
          return Response(serializer.data)
     
     elif request.method =='POST':
          data = request.data
          serializer = PeopleSerializer(data=data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)
          
     elif request.method == 'PUT':
          data = request.data
          obj = People.objects.get(id=data['id'])
          serializer = PeopleSerializer(obj,data=data)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)
    
     elif request.method == 'PATCH':
          data = request.data
          obj = People.objects.get(id=data['id'])
          serializer = PeopleSerializer(obj,data=data,partial=True)
          if serializer.is_valid():
               serializer.save()
               return Response(serializer.data)
          else:
               return Response(serializer.errors)
          
     elif request.method=='DELETE':
          data = request.data
          obj = People.objects.get(id=data['id'])
          obj.delete()
          return Response({"message":"Deleted successfully"})

