from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Handle,Category
from .serializers import HandleSerializer,CategorySerializer 
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    data = ['/handles','handles/:username']
    # return JsonResponse(data, safe=False); #safe word - lets JsonResponse read Python Dict files
    return Response(data)

# @api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
class HandlesList(APIView):
    # data = ['Kirtan', 'Mayank', 'Manav']
    def get(self,request,format=None):
        query = request.GET.get('query')

        handles = Handle.objects.filter(Q(username__icontains=query))

        serializer = HandleSerializer(handles, many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        handle = Handle.objects.create(
            rank = request.data['rank'],
            username = request.data['username'],
            channel_info = request.data['channel_info'],
            category_id = request.data['category_id'],
            posts = request.data['posts'],
            followers = request.data['followers'],
            avg_likes = request.data['avg_likes'],
            profile_pic = request.data['profile_pic']
        )

        serializer = HandleSerializer(handle, many=False)
        
        return Response(serializer.data)

class HandleDetails(APIView):
    def get_object(self, username):
        try:
            return Handle.objects.get(username=username)
        except Handle.DoesNotExist:
            raise JsonResponse("Handle Does Not Exists!")
    
    def get(self, request, username):
        # handle = Handle.objects.get(username = username)
        handle = self.get_object(username)
        serializer = HandleSerializer(handle,many=False)
        return Response(serializer.data)
    
    def put(self,request, username):
        # handle = Handle.objects.get(username = username)
        handle = self.get_object(username)      
        handle.rank = request.data['rank'],
        handle.username = request.data['username'] #edit this out with your api's data
        handle.channel_info = request.data['channel_info'],
        handle.profile_pic = request.data['profile_pic']
        handle.posts = request.data['posts'],
        handle.followers = request.data['followers'],
        handle.avg_likes = request.data['avg_likes'],
        handle.profile_pic = request.data['profile_pic']

        handle.save()
        serializer = HandleSerializer(handle,many=False)
        return Response(serializer.data)
    
    def delete(self,request,username):
        handle = self.get_object(username)
        handle.delete()
        return Response('User was deleted!')


@api_view(['GET'])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def category_filter(request):
    if request.method == 'GET':
        query = request.GET.get('query')
     
        handles = Handle.objects.filter(Q(category_id=query))

        serializer = HandleSerializer(handles, many=True)
        return Response(serializer.data)

