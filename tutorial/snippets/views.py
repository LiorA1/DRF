from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import mixins
from rest_framework import generics

from rest_framework import permissions


@csrf_exempt
def snippet_list(request):
	"""
	List all code snippets, or create a new snippet.
	"""
	if request.method == 'GET':
		snippets = Snippet.objects.all()
		serializer = SnippetSerializer(snippets, many=True)
		return JsonResponse(serializer.data, safe=False)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data, status=201)
		return JsonResponse(serializer.errors, status=400)


@api_view(['GET', 'POST'])
def snippet_list_second(request, format=None):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)  # Modified compared to previous

    elif request.method == 'POST':
        # data = JSONParser().parse(request)  # Modified
        serializer = SnippetSerializer(data=request.data)  # Modified
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED) # Modified

        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Modified


# Class-Based View -

# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """

#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# using-mixins -

class SnippetListM(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# using-generic-class-based-views -

class SnippetList(generics.ListCreateAPIView):
    """
        Used for read-write endpoints to represent a collection of model instances.
        Provides GET and POST method handlers.
        https://www.django-rest-framework.org/api-guide/generic-views/#listcreateapiview
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #! From rest_framework/views.py/APIView
    # https://github.com/encode/django-rest-framework/blob/b25ac6c5e36403f62b13163a0190eaa48b586c47/rest_framework/views.py#L104

    #* Allows modifications in the instance save management.
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

	





@csrf_exempt
def snippet_detail(request, pk):
	"""
	Retrieve, update or delete a code snippet.
	"""
	try:
		snippet = Snippet.objects.get(pk=pk)
	except Snippet.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = SnippetSerializer(snippet)
		return JsonResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = SnippetSerializer(snippet, data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse(serializer.data)
		return JsonResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		snippet.delete()
		return HttpResponse(status=204)


@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail_second(request, pk, format=None):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)  # Modified

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)  # Modified

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)  # Modified
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)  # Modified
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) # Modified

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # Modified


# Class-Based View -

class SnippetDetailC(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# using-mixins -

class SnippetDetailM(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# using-generic-class-based-views -
from snippets.permissions import IsOwnerOrReadOnly

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })


from rest_framework import renderers

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)



from rest_framework import viewsets

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides User `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer



from rest_framework.decorators import action

class SnippetViewSet(viewsets.ModelViewSet):
    """
    Lior: This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    premission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

