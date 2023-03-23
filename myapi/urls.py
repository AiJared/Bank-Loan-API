from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("myapi", views.ApprovalsView)

urlpatterns = [
    path("api/v1/", include(router.urls)),
    path('status/', views.approvereject),
]