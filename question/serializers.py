from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.cache import cache
from config.qiniu import get_token
from qiniu import put_data
from .models import Question
from django.conf import settings


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['version', 'url', 'course']


class QuestionUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['version', 'course', 'file']

    file = serializers.FileField()

    def create(self, validated_data):
        course = validated_data['course']
        version = validated_data['version']
        file_name = self._get_filename(course_name=course.id, version=version)
        file: InMemoryUploadedFile = validated_data['file']
        token = get_token()
        data = file.read()
        put_data(key=file_name, up_token=token, data=data, mime_type='application/json')
        url = settings.QINIU_HOST + '/' + file_name
        cache.set(course.get_course_version_key(), version)
        return Question.objects.create(url=url, course=course, version=version)

    def _get_filename(self, course_name, version):
        return f'{course_name}_{version}'
