from django.shortcuts import render, get_object_or_404
from rest_framework import status, mixins, generics, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from sample_app.chatgpt import generate_response
from sample_app.models import Snippet
from sample_app.permissions import IsOwnerOrReadOnly
from sample_app.serialize import SnippetSerializer, UserSerializer
from rest_framework import permissions

from django.http import JsonResponse


def chat(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        response = generate_response(user_message)
        return render(request, 'sample_app/chat.html', {'user_message': user_message, 'response': response})
    else:
        return render(request, 'sample_app/chat.html')


# class StudentView(APIView):
#
#     def get(self, request, id=None, format=None):
#         if id:
#             # Retrieve a single student by ID
#             student = Students.objects.get(pk=id)
#             serializers = StudentSerializer(student)
#             return Response({'success': 'success', "students": serializers.data}, status=200)
#         else:
#             # Retrieve a list of all students
#             queryset = Students.objects.all()
#             serializers = StudentSerializer(queryset, many=True)
#             return Response({'status': 'success', 'students': serializers.data}, status=200)
#
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         student = Students.objects.get(id=id)
#         serializer = StudentSerializer(student, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data})
#         else:
#             return Response({"status": "error", "data": serializer.errors})
#
#     def delete(self, request, id=None):
#         result = get_object_or_404(Students, id=id)
#         result.delete()
#         return Response({"status": "success", "data": "Record Deleted"})

# class StudentList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [JSONParser]

# class StudentDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
{
        "position": "Python Backend",
        "skills": "Critical thinking and problem solving",
        "name": "Exalt"
    }