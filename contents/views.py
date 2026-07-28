from django.shortcuts import get_object_or_404
from rest_framework import generics

from contents.models import AppConfig, Category, Video
from contents.serializers import (
    AppConfigSerializer,
    CategorySerializer,
    VideoSerializer,
)


class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True).order_by("name")
    serializer_class = CategorySerializer


class CategoryDetailAPi(generics.RetrieveAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class VideoListApi(generics.ListAPIView):
    queryset = Video.objects.filter(is_approved=True, is_active=True,).select_related('category').order_by('-create_at')
    serializer_class = VideoSerializer

class VideoDetailApi(generics.RetrieveAPIView):
    queryset = Video.objects.filter(is_approved=True, is_active=True,).select_related('category')
    serializer_class = VideoSerializer


class CategoryVideoListApi(generics.ListAPIView):
    serializer_class = VideoSerializer
    def get_queryset(self):
        category_id = self.kwargs['category_id']
        category = get_object_or_404(Category, id=category_id, is_active=True)
        return Video.objects.filter(
            category = category,
            is_approved = True,
            is_active =True,
        ).select_related('category').order_by('-create_at')
class AppConfigAPIView(
    generics.RetrieveAPIView
):

    serializer_class = (
        AppConfigSerializer
    )

    def get_object(self):

        config = (
            AppConfig.objects
            .first()
        )

        if not config:

            config = AppConfig.objects.create()

        return config