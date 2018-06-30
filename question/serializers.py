from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from config.qiniu import q, get_token, InputStream
from qiniu import put_stream
from .models import Question
from course.models import Course


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
        file_name = self._get_filename(course_name=course.name, version=validated_data['version'])
        file: InMemoryUploadedFile = validated_data['file']
        token = get_token(file_name)
        ret, info = put_stream(token, key=file_name, file_name=file_name,
                               input_stream=InputStream(file), data_size=file.size)
        print(ret, info)

    def _get_filename(self, course_name, version):
        return f'{course_name}_{version}'
