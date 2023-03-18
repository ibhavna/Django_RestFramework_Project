from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.

############################# CRUD VIEWS FOR STUDENT MODEL#######################################

@api_view(['GET', 'POST'])
def student_one(request):

    try:
        if request.method == 'POST':
            data = request.data
            serializer = StudentSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"True","message": "Successfully entered the data","data":serializer.data})
            else:
                return Response({"status":"False","message": "Please enter the data in correcr format","data":serializer.data})

        else:
            if request.method == 'GET':
                data = Student.objects.all()
                serializer = StudentSerializer(data, many=True)
                return Response({"data":serializer.data})

    except Exception as e :

        return Response({"status":"False","message": "Something went wrong","Error":str(e)})
    

@api_view(['PUT','DELETE'])
def student_two(request,id):

    try:
        if request.method == 'PUT': 
            data = Student.objects.get(id=id)
            serializer = StudentSerializer(instance=data,data= request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"True","message": "Successfully updated the data","data":serializer.data})

        else:
            if request.method == 'DELETE':
                data = Student.objects.get(id=id)
                data.delete()
                return Response({"status":"True","message":"successfully deleted the data"})
            
    except Exception as e :

        return Response({"status":"False","message": "Something went wrong","Error":str(e)})
    
    
######################################################CRUD Views for School model#######################################################

@api_view(['GET', 'POST'])
def school_one(request):

    try:
        if request.method == 'POST':
            data = request.data
            serializer = SchoolSerializer(data=data)
            
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"True","message": "Successfully entered the data","data":serializer.data})
            else:
                return Response({"status":"False","message": "Please enter the data in correcr format","data":serializer.data})

        else:
            if request.method == 'GET':
                data = School.objects.all()
                serializer = SchoolSerializer(data, many=True)
                return Response({"data":serializer.data})

    except Exception as e :

        return Response({"status":"False","message": "Something went wrong","Error":str(e)})
    

@api_view(['PUT','DELETE'])
def school_two(request,id):

    try:
        if request.method == 'PUT': 
            data = School.objects.get(id=id)
            serializer = SchoolSerializer(instance=data,data= request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({"status":"True","message": "Successfully updated the data","data":serializer.data})
            else:
                return Response({"status":"False","message": "Please enter the data in correcr format","data":serializer.data})

        else:
            if request.method == 'DELETE':
                data = School.objects.get(id=id)
                data.delete()
                return Response({"status":"True","message":"successfully deleted the data"})
            
    except Exception as e :

        return Response({"status":"False","message": "Something went wrong","Error":str(e)})
    

##################################Gets school data with students under that school#############################

@api_view(['GET'])
def get_school_data(request,id):
    try:
        data = Student.objects.filter(school=id)
        serializer = StudentSerializer(data, many=True)
        return Response({"status":"True","message": "Sucess","Data":serializer.data})
 
    except Exception as e :
            return Response({"status":"False","message": "Something went wrong","Error":str(e)})

