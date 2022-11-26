from rest_framework import routers
from .views import UploadViewSet
from .api import UsersViewSet, DocumentsViewSet, RepositoriesViewSet


router = routers.DefaultRouter()
router.register('users', UsersViewSet)
router.register('documents', DocumentsViewSet)
router.register('repositories', RepositoriesViewSet)
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = router.urls