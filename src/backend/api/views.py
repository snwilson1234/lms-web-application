from django.contrib.auth.models import Group, User
from api.models import Course
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from api.serializers import CourseSerializer, GroupSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseViewSet(viewsets.ViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    # queryset = Course.objects.all().order_by('title')
    # serializer_class = CourseSerializer
    # permission_classes = [permissions.]
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        queryset = Course.objects.all().order_by('title')
        response = [{'id': course.id,'title': course.title, 'term': course.term} for course in queryset]
        return Response(response)

    def create(self, request):
        serializer = CourseSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)

        title = serializer.validated_data.get('title')
        term = serializer.validated_data.get('term')

        course = Course.objects.create(
            title=title,
            term=term
        )

        return Response(True)

    def retrieve(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        try:
            course = Course.objects.get(pk=pk).delete()
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(True)
