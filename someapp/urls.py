from rest_framework.routers import DefaultRouter
from .views import ManufacturerViewsets, ProductViewsets

router = DefaultRouter()
router.register('manufacturer', ManufacturerViewsets, basename='manufacturer')
router.register('product', ProductViewsets, basename='product')

urlpatterns = router.get_urls()