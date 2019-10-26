

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.UserView)
router.register('user/<str:username>', views.UserView)

urlpatterns = [
    path(r'API/v1/', include(router.urls))
]
