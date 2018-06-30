from qiniu import Auth
from django.conf import settings

q = Auth(settings.QINIU_ACCESS_KEY, settings.QINIU_SECRET_KEY)


def get_token(expire_time=3600):
    return q.upload_token(bucket='xuebasizheng', expires=expire_time)
