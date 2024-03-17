from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from user.models import User
from service.models import Service, Job
from rest_framework import permissions, viewsets, generics, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from api.serializers import GroupSerializer, UserSerializer, ServiceSerializer, JobSerializer, ContractSerializer, TaskSerializer
from contract.models import Contract, Task


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        """
        Sobrescribe el método `get_queryset` para filtrar los trabajos
        basados en el servicio proporcionado en la URL.
        """
        service_id = self.kwargs['service_id']  # Obtén el ID del servicio de la URL
        return Job.objects.filter(service_id=service_id)
    
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        contract_id = self.kwargs['contract_id']  # Obtén el ID del servicio de la URL
        return Task.objects.filter(contract_id=contract_id)
    

class UserServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user_id = self.kwargs['user_id']  # Obtén el ID del servicio de la URL
        return Service.objects.filter(user_id=user_id)

class ContractViewSetnt(viewsets.ModelViewSet):
    queryset=Contract.objects.all()
    serializer_class=ContractSerializer   
    # permission_classes = [permissions.IsAuthenticated]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ContractViewSet(viewsets.ModelViewSet):
    serializer_class=ContractSerializer   
    queryset=Contract.objects.all()
    
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response("missing user", status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def test_token(request):
    return Response("passed for {}" .format(request.user.username))

@api_view(['POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response("Successfully logged out.")
