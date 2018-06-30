from qiniu import Auth
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile

q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


def get_token(file_name, expire_time=3600):
    return q.upload_token(bucket='xuebasizheng', key=file_name, expires=expire_time)


class InputStream:
    def __init__(self, file: InMemoryUploadedFile):
        self.file = file

    def read(self, chunk_size):
        q = b''.join(list(self.file.chunks(chunk_size)))
        return q

    def seek(self, *args, **kwargs):
        return self.file.seek(*args, **kwargs)
