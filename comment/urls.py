from django.urls import path, include
from .views import CommentView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', CommentView)

urlpatterns =[
    path('', include(router.urls))
]
