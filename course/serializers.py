from rest_framework import serializers
from .models import Course
from question.serializers import QuestionSerializer


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'questions']

    questions = QuestionSerializer(source='get_current_questions', read_only=True)
