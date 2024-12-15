from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import AttributeSerializer


class AttributeCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AttributeSerializer(data=request.data)

        if serializer.is_valid():
            # Обработка данных через сериализатор
            processed_data = serializer.data
            return Response(processed_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
