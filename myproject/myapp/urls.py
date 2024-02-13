from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('api/upload/image/', ImageUploadView.as_view(), name='image_upload'),
]
