from django.contrib import admin
from django.core.exceptions import ValidationError

from contents.forms import VideoAdminForm
from contents.yotube_service import *
from contents.youtube_utils import *

from .models import AppConfig, Category, Video

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active', 'create_at',)
    prepopulated_fields = {'slug': ('name',)}  # noqa: RUF012
    list_filter = ('is_active',)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    forms = VideoAdminForm
    list_display = ('category', 'title', 'channel_title', 'youtube_video_id', 'is_approved', 'is_active', 'create_at',)
    list_filter = (
        "category", 
        "is_approved", 
        "is_active",)
    list_editable = ('is_approved', 'is_active',)
    search_fields =  ('title', 'youtube_video_id', 'channel_title',)
    readonly_fields = ('youtube_video_id', 'title', 'description', 'thumbnail_url', 'channel_title', 'duration',)

    def save_model(self, request, obj, form, change):

         video_id = extract_youtube_video_id(obj.youtube_url)

         if not video_id:
            raise ValidationError("Invaild Url")
         existing_video = Video.objects.filter(youtube_video_id=video_id).exclude(pk=obj.pk).first()
         if existing_video:
            raise ValidationError("This Video already exists")
         youtube_data = fetch_youtube_video(video_id)
         if not youtube_data:
            raise ValidationError("Youtube Video not found")
         if (youtube_data["privacy_status"] != "public" ):
            raise ValidationError("Only Public video allowed")
         if not youtube_data['embeddable']:
            raise ValidationError("This video is not embeddable")
         obj.youtube_video_id = (video_id)
         obj.title = youtube_data['title']
         obj.description = youtube_data['description']
         obj.thumbnail_url = youtube_data['thumbnail_url']
         obj.channel_title = youtube_data['channel_title']
         obj.duration = youtube_data['duration']
         return super().save_model(request, obj, form, change)

@admin.register(AppConfig)
class AppConfigAdmin(
    admin.ModelAdmin
):

    list_display = (
        "app_name",
        "maintenance_mode",
        "updated_at",
    )

    fieldsets = (

        (
            "App Information",
            {
                "fields": (
                    "app_name",
                    "app_logo",
                ),
            },
        ),

        (
            "Theme",
            {
                "fields": (
                    "primary_color",
                    "secondary_color",
                ),
            },
        ),

        (
            "Maintenance",
            {
                "fields": (
                    "maintenance_mode",
                    "maintenance_message",
                ),
            },
        ),

        (
            "Features",
            {
                "fields": (
                    "enable_screen_time",
                    "enable_watch_history",
                    "enable_parent_mode",
                ),
            },
        ),

    )