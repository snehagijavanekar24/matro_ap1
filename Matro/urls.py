from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import SimpleRouter
from app1.views import MemberViewSet

router=SimpleRouter()
router.register('member',MemberViewSet,basename='member')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a1/',include(router.urls))
]
