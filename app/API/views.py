from rest_framework import generics, viewsets

from .serializer import PositionSerializer, EmployeeSerializer
from .models import Position, Employee


class PositionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class PositionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def get_queryset(self):
        return super().get_queryset().filter(id=self.kwargs.get('pk'))


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
