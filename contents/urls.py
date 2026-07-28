from django.urls import path

from contents.views import (
    AppConfigAPIView,
    CategoryDetailAPi,
    CategoryListApi,
    CategoryVideoListApi,
    VideoDetailApi,
    VideoListApi,
)

urlpatterns = [
    path("categories/", CategoryListApi.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailAPi.as_view(), name="category-detail"),
    path("videos/", VideoListApi.as_view(), name="approved-video-list"),
    path("videos/<int:pk>/", VideoDetailApi.as_view(), name="approved-video-detail"),
    path("categories/<int:category_id>/videos/", CategoryVideoListApi.as_view(), name="category-video-list"),
    path("config/", AppConfigAPIView.as_view(), name="app-config")
]
