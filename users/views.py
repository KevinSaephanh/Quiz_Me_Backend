from django.shortcuts import render
from rest_framework import viewsets, views, permissions, status, pagination
from rest_framework.decorators import permission_classes, api_view, authentication_classes
from .models import CustomUser
from .serializers import UserSerializer
from quiz_me.permissions import IsOwnerOrReadOnly
from requests.models import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


@api_view(['GET'])
@permission_classes([permissions.IsAdminUser])
def user_list(request, page):
    try:
        queryset = CustomUser.objects.all()
    except CustomUser.DoesNotExist:
        return Response({'error': 'No profiles found'}, status=status.HTTP_404_NOT_FOUND)

    # Set up pagination for users
    paginator = pagination.PageNumberPagination()
    paginator.page_size = 10
    paginator.page = page

    # Create paginated user list
    paginated_users = paginator.paginate_queryset(queryset, request)
    serializer = UserSerializer(paginated_users, many=True)
    if serializer is not None:
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


class UserViewSet(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    authentication_classes = [JSONWebTokenAuthentication]

    # Used for retrieve, update, and destroy methods
    def get_queryset(self, pk):
        try:
            queryset = CustomUser.objects.filter(pk=pk)
            return queryset
        except CustomUser.DoesNotExist:
            raise Exception('Quiz does not exist')

    def retrieve(self, request, pk):
        user = self.get_queryset(pk)
        serializer = self.serializer_class(user)
        if serializer is not None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk):
        data = request.data
        user = self.serializer_class.update(request, pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer is not None:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, pk):
        user = self.get_queryset(pk)
        if user is not None and user is not None:
            user.delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
