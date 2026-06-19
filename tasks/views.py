from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner
from .models import Task
from .serializers import TaskSerializer
from .pagination import TaskPagination



class TaskListCreateView(generics.ListCreateAPIView):
    
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
    pagination_class = TaskPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'description', 'status']
    
        

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsOwner]