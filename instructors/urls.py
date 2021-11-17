from rest_framework.routers import DefaultRouter
from instructors.views import InstructorViewSet

router = DefaultRouter()
router.register('instructors', InstructorViewSet)

urlpatterns = router.urls