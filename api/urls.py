from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.viewsets import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='tasks')

urlpatterns = [
    path('', include(router.urls)),
    # path('auth/callback/', callback, name='callback'),
]
