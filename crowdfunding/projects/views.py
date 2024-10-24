from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly
from django.http import Http404
from .models import Project, Pledge, Like
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
       project = self.get_object(pk)
       serializer = ProjectDetailSerializer(project)
       return Response(serializer.data)
    
    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

class PledgeList(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PledgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(
            instance=pledge,
            data=request.data,
            partial=True  
        )
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LikeProject(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get_project(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            return project
        except Project.DoesNotExist:
            raise Http404("Project not found")

    def post(self, request, pk):
        # Fetch project using get_project() and handle 404 manually
        project = self.get_project(pk)
        
        # Check if the user has already liked the project
        if Like.objects.filter(user=request.user, project=project).exists():
            return Response({'error': 'You already liked this project!'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a like
        Like.objects.create(user=request.user, project=project)
        return Response({'message': 'Project liked!'}, status=status.HTTP_201_CREATED)
    

class UnlikeProject(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
        ]

    def get_project(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            return project
        except Project.DoesNotExist:
            raise Http404("Project not found")

    def delete(self, request, pk):
        # Fetch project using get_project() and handle 404 manually
        project = self.get_project(pk)

        # Check if the user has liked the project before
        like = Like.objects.filter(user=request.user, project=project).first()
        if like:
            like.delete()
            return Response({'message': 'Project unliked!'}, status=status.HTTP_200_OK)
        
        return Response({'error': 'You haven’t liked this project yet!'}, status=status.HTTP_400_BAD_REQUEST)
    