from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Advocate
from .serializers import AdvocateSerializer
from django.db.models import Q

@api_view(['GET'])
def endpoints(request):
    data = ['/advocates','advocates/:username']
    # return JsonResponse(data, safe=False) #safe word - lets JsonResponse read Python Dict files
    return Response(data)

@api_view(['GET','POST'])
def advocates_list(request):
    # data = ['Kirtan', 'Mayank', 'Manav']
    if request.method == 'GET':
        query = request.GET.get('query')

        if query == None:
            query = ''

        advocates = Advocate.objects.filter(Q(username__icontains=query) |   Q(bio__icontains=query))
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        advocate = Advocate.objects.create(
            username = request.data['username'],
            bio = request.data['bio']
        )

        serializer = AdvocateSerializer(advocate, many=False)
        
        return Response(serializer.data)

# @api_view(['GET', 'PUT', 'DELETE'])
# def advocates_details(request,username):
#     # data = username
#     advocate = Advocate.objects.get(username = username)
#     if request.method == 'GET':
#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         advocate.username = request.data['username'] #edit this out with your api's data
#         advocate.bio = request.data['bio']

#         advocate.save()
#         serializer = AdvocateSerializer(advocate,many=False)
#         return Response(serializer.data)
    
#     if request.method == 'DELETE':
#         advocate.delete()
#         return Response('User was deleted!')

class AdvocateDetails(APIView):
    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise JsonResponse("Advocate Does Not Exists!")
    
    def get(self, request, username):
        # advocate = Advocate.objects.get(username = username)
        advocate = self.get_object(username)
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    
    def put(self,request, username):
        # advocate = Advocate.objects.get(username = username)
        advocate  = self.get_object(username)
        advocate.username = request.data['username'] #edit this out with your api's data
        advocate.bio = request.data['bio']

        advocate.save()
        serializer = AdvocateSerializer(advocate,many=False)
        return Response(serializer.data)
    
    def delete(self,request,username):
        advocate = self.get_object(username)
        advocate.delete()
        return Response('User was deleted!')





