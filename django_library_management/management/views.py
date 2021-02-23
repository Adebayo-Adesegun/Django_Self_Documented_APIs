from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from .serializers import BookSerializer, CatalogueSerializer
from .models import Book, Catalogue
from rest_framework.parsers import JSONParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='get', operation_description="Describe get operation")
@swagger_auto_schema(method = 'post',operation_description="Describe post operation", request_body=CatalogueSerializer)
@swagger_auto_schema(method = 'delete',operation_description="Describe delete operation")
@api_view(['GET', 'POST', 'DELETE'])
def catalogue_list(request):
    # Get List of Catalogues, Post a new Catalogue and Delete a Catalogue
 
    if request.method == 'GET':
        catalogues = Catalogue.objects.all()
 
        catalogue_name = request.GET.get('name', None)
        if catalogue_name is not None:
            catalogues = Catalogue.filter(name__icontains=catalogue_name)
 
        catalogue_serializer = CatalogueSerializer(catalogues, many=True, context={'request': request})
        return JsonResponse(catalogue_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        catalogue_data = JSONParser().parse(request)
 
        catalogue_serializer = CatalogueSerializer(data=catalogue_data, context={'request': request})
 
        if catalogue_serializer.is_valid():
            print(request.user)
            catalogue_serializer.create(catalogue_data)
            return JsonResponse(catalogue_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(catalogue_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Catalogue.objects().delete()
        return JsonResponse({'message' : '{} Catalogues were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method ='get', operation_description="Describe get by Id operation")
@swagger_auto_schema(method = 'put',operation_description="Describe update by Id operation", request_body=CatalogueSerializer)
@swagger_auto_schema(method = 'delete',operation_description="Describe delete by Id operation")
@api_view(['GET', 'PUT', 'DELETE'])
def catalogue_detail(request, pk):
    #find catalogue by primary key
    try:
        catalogue = Catalogue.objects.get(pk=pk)
        if request.method == 'GET':            
            catalogue_serializer = CatalogueSerializer(catalogue)
            return JsonResponse(catalogue_serializer.data)
 
        elif request.method == 'PUT':
            catalogue_data = JSONParser().parse(request)
            catalogue_serializer = CatalogueSerializer(catalogue, data=catalogue_data)
 
            if catalogue_serializer.is_valid():
                catalogue_serializer.save()
                return JsonResponse(catalogue_serializer.data)
            return JsonResponse(catalogue_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
 
        elif request.method == 'DELETE':
            catalogue.delete()
            return JsonResponse({'message' : 'Catalogue was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
 
    except Catalogue.DoesNotExist:
        return JsonResponse({'message': 'The catalogue does not exist'})

@swagger_auto_schema(method='get', operation_description="Describe get operation")
@swagger_auto_schema(method = 'post',operation_description="Describe post operation", request_body=BookSerializer)
@swagger_auto_schema(method = 'delete',operation_description="Describe delete operation")
@api_view(['GET', 'POST', 'DELETE'])
def book_list(request): 
 
    if request.method == 'GET':
        books = Book.objects.all()
 
        book_name = request.GET.get('name', None)
        if book_name is not None:
            books = Catalogue.filter(name__icontains=book_name)
 
        book_serializer = BookSerializer(books, many=True, context={'request': request})
        return JsonResponse(book_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        book_data = JSONParser().parse(request)
 
        book_serializer = BookSerializer(data=book_data, context={'request': request})
 
        if book_serializer.is_valid():
            print(request.user)
            book_serializer.create(book_data)
            return JsonResponse(book_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(book_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Book.objects().delete()
        return JsonResponse({'message' : '{} Books were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method ='get', operation_description="Describe get by Id operation")
@swagger_auto_schema(method = 'put',operation_description="Describe update by Id operation", request_body=BookSerializer)
@swagger_auto_schema(method = 'delete',operation_description="Describe delete by Id operation")
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    #find Book by primary key
    try:
        book = Book.objects.get(pk=pk)
        if request.method == 'GET':
            book_serializer = BookSerializer(book)
            return JsonResponse(book_serializer.data)
 
        elif request.method == 'PUT':
            book_data = JSONParser().parse(request)
            book_serializer = CatalogueSerializer(book, data=book_data)
 
            if book_serializer.is_valid():
                book_serializer.save()
                return JsonResponse(book_serializer.data)
            return JsonResponse(book_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            book.delete()
            return JsonResponse({'message' : 'Book was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
 
 
    except Book.DoesNotExist:
        return JsonResponse({'message': 'The book does not exist'})



        


