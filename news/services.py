import os
import uuid
from urllib.parse import urljoin
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class CkeditorCustomStorage(FileSystemStorage):
    def get_valid_name(self, name: str) -> str:
        return uuid.uuid4().hex + "__" + name

    def _save(self, name, content):
        name = os.path.join("news", self.get_valid_name(name))
        return super()._save(name, content)

    location = os.path.join(settings.MEDIA_ROOT, "uploads/")

    base_url = urljoin(settings.MEDIA_URL, "uploads/")
