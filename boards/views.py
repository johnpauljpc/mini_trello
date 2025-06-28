from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .serializers import BoardSerializer, CreateBoardSerializer
from .permissions import IsOwner
from .models import USER, Board

# Create your views here.
class CreateListBoard(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateBoardSerializer
        return BoardSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Board.objects.filter(owner=user)
        return Board.objects.filter(visibility = "public") #unauthenticated users can view the list public boards
    


class DetailBoard(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwner]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BoardSerializer
        return CreateBoardSerializer
    

        