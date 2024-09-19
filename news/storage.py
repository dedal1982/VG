from django.conf import settings
from django.core.files.storage import FileSystemStorage


class MediaStorage(FileSystemStorage):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("location", settings.MEDIA_ROOT)
        super().__init__(*args, **kwargs)
