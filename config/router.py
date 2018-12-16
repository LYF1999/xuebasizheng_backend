from rest_framework import routers
from course.views import CourseViewSet
from user.views import UserViewSet
from question.views import QuestionViewSet

router = routers.DefaultRouter()

router.register(r'user', UserViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'questions', QuestionViewSet)