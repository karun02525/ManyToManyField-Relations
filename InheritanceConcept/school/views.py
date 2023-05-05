from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import response,status
from .models import Student,Teacher,ProxyStudent,Song,Post
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

def home(request):
    
   song= Song.objects.filter(user__username='karun')
   for i in song:
    print(i.song_name,i.song_duration,i.user)
   
   
   data = Student.objects.all()
   #proxy_data= ProxyStudent.str.get_roll_range(100,300)
   proxy_data= ProxyStudent.str.all()
   return render(request,'index.html',{'students':data,'proxy_students':proxy_data})

@api_view(['POST'])
def create(request):
    serializer  = StudentSerializer(data=request.data)
    if not serializer.is_valid():
        return Response({'status':False,'message':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    return Response({'status':True,'message':'successfull create','data':serializer.data},status=status.HTTP_200_OK)

@api_view(['GET'])
def get(request):
    query_set = Student.objects.all()
    serializer = StudentSerializer(query_set,many=True)
    return Response({'status':True,'data':serializer.data},status=status.HTTP_200_OK)
