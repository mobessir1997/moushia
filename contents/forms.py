from django import forms

from contents.models import Video
from contents.yotube_service import *
from contents.youtube_utils import *


class VideoAdminForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [  # noqa: RUF012
            'category', 'youtube_url', 'is_active', 'is_approved'
        ]
    