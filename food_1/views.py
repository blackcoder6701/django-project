from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse
from food_1.models import First
from food_1.serializers import Foody
from rest_framework import status 
from rest_framework.response import Response
from rest_framework import mixins

# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView
# from rest_framework.parsers import JSONParser


class firstnew():

    class Snippetlist(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
        queryset=First.objects.all()
        serializer_class= Foody
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Snippetdetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=First.objects.all()
    serializer_class=Foody

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
  
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs) 


# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
# class SnippetList(generics.ListCreateAPIView):
#     queryset = First.objects.all()
#     serializer_class = SnippetSeri


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


#--------------------------------------
'''using the class based method'''
# class Firstone(APIView):
#     def get(self,request,format=None):
#         snippet= First.objects.all()
#         serializer= Foody(snippet,many=True)
#         return Response(serializer.data)
    
#     def post(self,request,format=None):
#         serializer=Foody(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=201)
#         return Response(serializer.errors,status=400)


# @api_view(['GET','POST','DELETE'])
# def firstone(request,pk,format=None):
#     try:
#         num = First.objects.get(pk=pk)
#         print(num)
#     except First.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         userall= Foody(num)
#         # validate_data=Foody(userall,many=True)
#         print(userall)
#         return Response(userall.data)
    
#     elif request.method == 'POST':
#         result=Foody(num,data=request.data)
#         if result.is_valid():
#             result.save()
#             return Response(result.data,status=201)
#         return Response(result.errors,status=400)

    # elif request.method == 'DELETE':
    #     num.delete()
    #     return Response(status=204)

#----------------------------------------------------------------- 

''' this was using the csrf decoraters '''
'''@csrf_exempt
def first_list(request):
    if request.method=='GET':
        userall= First.objects.all()
        validate_data=Foody(userall, many=True)
        return JsonResponse(validate_data.data, safe=False) 

    elif request.method == 'POST':
        data =JSONParser().parse(request)
        validate_data_new = Foody(data=data)
        if validate_data_new.is_valid():
            validate_data_new.save()
            return JsonResponse(validate_data_new.data ,status=201)
        return JsonResponse(validate_data_new.errors, status=400)'''

        
