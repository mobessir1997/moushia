from rest_framework import serializers

from contents.models import AppConfig, Category, Video


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']  # noqa: RUF012

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'category', 'title', 'youtube_video_id', 'description', 'thumbnail_url', 'duration']  # noqa: RUF012
class AppConfigSerializer(
    serializers.ModelSerializer
):

    class Meta:

        model = AppConfig

        fields = [  # noqa: RUF012
            "app_name",
            "app_logo",
            "primary_color",
            "secondary_color",
            "maintenance_mode",
            "maintenance_message",
            "enable_screen_time",
            "enable_watch_history",
            "enable_parent_mode",
        ]