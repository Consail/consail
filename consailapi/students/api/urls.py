from rest_framework.routers import DefaultRouter

from consailapi.students.api.views import StudentViewSet

router = DefaultRouter()

router.register("students", StudentViewSet, basename="students")

urlpatterns = [] + router.urls
