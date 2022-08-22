from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers
from . import views
from pprint import pprint

router = SimpleRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('carts', views.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='product-reviews')

carts_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart') #this gives us a parameter cart_pk
carts_router.register('items', views.CartItemViewSet, basename='cart-items')
# pprint(products_router.urls)
urlpatterns = router.urls + products_router.urls + carts_router.urls