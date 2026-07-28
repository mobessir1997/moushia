from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "categorires"

    def __str__(self):
        return self.name

class Video(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=250)
    youtube_url = models.URLField(max_length=500, unique=True)
    youtube_video_id = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True)
    thumbnail_url = models.CharField(blank=True, unique=True)
    channel_title = models.CharField(max_length=500, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    is_approved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class AppConfig(models.Model):

    app_name = models.CharField(
        max_length=100,
        default="Kids Learning",
    )

    app_logo = models.URLField(
        blank=True,
    )

    primary_color = models.CharField(
        max_length=20,
        default="#4CAF50",
    )

    secondary_color = models.CharField(
        max_length=20,
        default="#FFFFFF",
    )

    maintenance_mode = models.BooleanField(
        default=False,
    )

    maintenance_message = models.TextField(
        blank=True,
        default=(
            "The app is temporarily "
            "under maintenance."
        ),
    )

    enable_screen_time = models.BooleanField(
        default=False,
    )

    enable_watch_history = models.BooleanField(
        default=False,
    )

    enable_parent_mode = models.BooleanField(
        default=False,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )
    def save(self,*args,**kwargs,):
            self.pk = 1

            super().save(*args,*kwargs,)

    def __str__(self):
        return self.app_name