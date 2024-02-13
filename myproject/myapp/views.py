from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *

class ImageUploadView(APIView):
    
    serializer_class = UploadedImageSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = UploadedImageSerializer(data=request.data)
        if serializer.is_valid():
            #uploaded_image = serializer.save()
            image_size = request.FILES['image'].size
            #file_path = uploaded_image.image.path  
            return Response({'image_size': image_size}, status=status.HTTP_201_CREATED)
            #return Response({'image_size': image_size, 'file_path': file_path}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
