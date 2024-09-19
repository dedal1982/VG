import uuid


def get_filename(filename, request):
    return f"{uuid.uuid4().hex}__{filename}"
