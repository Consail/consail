from django.urls import include, path

urlpatterns = [
    path("", include("consailapi.users.api.urls")),
    path("", include("consailapi.teachers.api.urls")),
]
